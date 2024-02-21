import unittest
from decimal import Decimal
from unittest.mock import AsyncMock, patch
from src.services import CurrencyService


class TestCurrencyService(unittest.IsolatedAsyncioTestCase):

    @patch("aiohttp.ClientSession.get")
    async def test_get_exchange_rates(self, mock_get):
        mock_get.return_value.__aenter__.return_value.json = AsyncMock(
            return_value={"conversion_rates": {"EUR": 0.85, "GBP": 0.73}}
        )

        currency_service = CurrencyService(api_key="")
        exchange_rates = await currency_service.get_exchange_rates()

        self.assertIsInstance(exchange_rates, dict)
        self.assertEqual(len(exchange_rates), 2)
        self.assertTrue("EUR" in exchange_rates)
        self.assertTrue("GBP" in exchange_rates)
        self.assertEqual(exchange_rates["EUR"], Decimal("0.85"))
        self.assertEqual(exchange_rates["GBP"], Decimal("0.73"))
