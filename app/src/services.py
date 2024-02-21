import aiohttp

from decimal import Decimal


class CurrencyService:
    def __init__(self, api_key: str):
        self.base_url = "https://v6.exchangerate-api.com/v6"
        self.api_key = api_key

    async def get_exchange_rates(self) -> dict[str, Decimal]:
        result = {}
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}/{self.api_key}/latest/USD"
            async with session.get(url) as response:
                json = await response.json()
                for code, rate in json["conversion_rates"].items():
                    result[code] = Decimal(str(rate))
                return result
