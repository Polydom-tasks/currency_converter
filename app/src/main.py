from fastapi import HTTPException, FastAPI, Depends

from schemas import CurrencySchema
from services import CurrencyService
from settings import settings
from store import CurrencyStore
from db import async_session, init_db
from decimal import Decimal

app = FastAPI()


def get_currency_store() -> CurrencyStore:
    return CurrencyStore(async_session)


def get_currency_service() -> CurrencyService:
    return CurrencyService(settings.API_KEY)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/currencies", response_model=list[CurrencySchema])
async def get_currencies(currency_store: CurrencyStore = Depends(get_currency_store)):
    currencies = await currency_store.get_currencies()
    currency_schemas = [CurrencySchema.from_orm(c) for c in currencies]
    return currency_schemas


@app.post("/update_rates")
async def update_exchange_rates(
    currency_service: CurrencyService = Depends(get_currency_service), currency_store: CurrencyStore = Depends(get_currency_store)
):
    exchange_rates = await currency_service.get_exchange_rates()
    await currency_store.update_currencies(exchange_rates)
    return {"message": "Exchange rates updated successfully"}


@app.get("/last_update")
async def get_last_update_time(currency_store: CurrencyStore = Depends(get_currency_store)):
    currency = await currency_store.get_currency_by_code("USD")
    return {"updated_at": currency.updated_at}


@app.get("/convert")
async def convert_currency(source: str, target: str, amount: Decimal, currency_store: CurrencyStore = Depends(get_currency_store)):
    source_currency = await currency_store.get_currency_by_code(source)
    if not source_currency:
        return HTTPException(404, {"error": "Source currency not found"})

    target_currency = await currency_store.get_currency_by_code(target)
    if not target_currency:
        return HTTPException(404, {"error": "Target currency not found"})

    rate = target_currency.rate / source_currency.rate
    result = amount * rate
    return {"converted_amount": result}
