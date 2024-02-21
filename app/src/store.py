from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Currency
from decimal import Decimal
from datetime import datetime


class CurrencyStore:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_currencies(self):
        async with self.session() as session:
            result = await session.execute(select(Currency))
            return result.scalars().all()

    async def get_currency_by_code(self, currency_code: str):
        async with self.session() as session:
            result = await session.execute(
                select(Currency).where(Currency.code == currency_code)
            )
            return result.scalar()

    async def update_currencies(self, new_rates: dict[str, Decimal]):
        async with self.session() as session:
            async with session.begin():
                update_time = datetime.now()
                for code, rate in new_rates.items():
                    result = await session.execute(
                        select(Currency).where(Currency.code == code)
                    )
                    currency = result.scalar()
                    if currency:
                        currency.rate = rate
                        currency.updated_at = update_time
                await session.commit()
