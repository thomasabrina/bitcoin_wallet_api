import unittest
from unittest.mock import patch
from app.utils import fetch_eur_to_btc_rate

class TestUtils(unittest.TestCase):
    @patch('app.utils.requests.get')
    def test_fetch_eur_to_btc_rate_success(self, mock_get):
        # Mock the response of requests.get to return a specific payload
        mock_get.return_value.json.return_value = {
            "data": [
                {"symbol": "BTC/EUR", "value": "12345.67"}
            ]
        }

        rate = fetch_eur_to_btc_rate()
        self.assertEqual(rate, 12345.67)

    @patch('app.utils.requests.get')
    def test_fetch_eur_to_btc_rate_not_found(self, mock_get):
        # Mock the response to simulate the rate not being found
        mock_get.return_value.json.return_value = {
            "data": [
                {"symbol": "ETH/EUR", "value": "234.56"}
            ]
        }

        rate = fetch_eur_to_btc_rate()
        self.assertIsNone(rate)

    @patch('app.utils.requests.get')
    def test_fetch_eur_to_btc_rate_exception(self, mock_get):
        # Mock requests.get to raise an exception
        mock_get.side_effect = Exception("An error occurred")

        rate = fetch_eur_to_btc_rate()
        self.assertIsNone(rate)

if __name__ == '__main__':
    unittest.main()