import datetime
from unittest.mock import patch

import pytest
import requests

from A005.mercado_bitcoin.apis import DaySummaryApi, TradesApi, MercadoBitcoinApi


class TestDaySummaryApi:

    @pytest.mark.parametrize(
        "coin, date, expected",
        [
            ("BTC", datetime.date(2022, 8, 20), "https://www.mercadobitcoin.net/api/BTC/day-summary/2022/8/20"),
            ("ETH", datetime.date(2022, 8, 20), "https://www.mercadobitcoin.net/api/ETH/day-summary/2022/8/20"),
            ("ETH", datetime.date(2022, 8, 21), "https://www.mercadobitcoin.net/api/ETH/day-summary/2022/8/21")
        ]
    )
    def test_get_endpoint(self, coin, date, expected):
        actual = DaySummaryApi(coin=coin)._get_endpoint(date=date)
        assert actual == expected


class TestTradesApi:

    @pytest.mark.parametrize(
        "coin, date_from, date_to, expected",
        [
            ("TEST", datetime.datetime(2022, 8, 19), datetime.datetime(2022, 8, 20),
             "https://www.mercadobitcoin.net/api/TEST/trades/1660878000/1660964400"),
            ("TEST", datetime.datetime(2022, 7, 15), datetime.datetime(2022, 8, 1),
             "https://www.mercadobitcoin.net/api/TEST/trades/1657854000/1659322800"),
            ("TEST", None, None,
             "https://www.mercadobitcoin.net/api/TEST/trades"),
            ("TEST", None, datetime.datetime(2022, 8, 1),
             "https://www.mercadobitcoin.net/api/TEST/trades"),
            ("TEST", datetime.datetime(2022, 7, 15), None,
             "https://www.mercadobitcoin.net/api/TEST/trades/1657854000"),
        ]
    )
    def test_get_endpoint(self, coin, date_from, date_to, expected):
        actual = TradesApi(coin=coin)._get_endpoint(date_from=date_from, date_to=date_to)
        assert actual == expected

    def test_get_endpoint_date_from_greater_than_date_to(self):
        with pytest.raises(RuntimeError):
            TradesApi(coin="TEST")._get_endpoint(
                date_from=datetime.datetime(2022, 8, 1),
                date_to=datetime.datetime(2022, 7, 15)
            )

    @pytest.mark.parametrize(
        "date, expected",
        [
            (datetime.datetime(2022, 8, 20), 1660964400),
            (datetime.datetime(2022, 8, 19), 1660878000),
            (datetime.datetime(2022, 7, 15), 1657854000),
            (datetime.datetime(2022, 7, 15, 0, 0, 5), 1657854005),
            (datetime.datetime(2022, 8, 1), 1659322800)
        ]
    )
    def test_get_unix_epoch(self, date, expected):
        actual = TradesApi(coin="TESTE")._get_unix_epoch(date)
        assert actual == expected


@pytest.fixture()
@patch("A005.mercado_bitcoin.apis.MercadoBitcoinApi.__abstractmethods__", set())
def fix_mercado_bitcoin_api():
    return MercadoBitcoinApi(
        coin="test"
    )


def mocked_requests_get(*args, **kwargs):
    class MockResponse(requests.Response):
        def __init__(self, json_data, status_code):
            super().__init__()
            self.status_code = status_code
            self.json_data = json_data

        def json(self):
            return self.json_data

        def raise_for_status(self) -> None:
            if self.status_code != 200:
                raise Exception

    if args[0] == "valid_endpoint":
        return MockResponse(json_data={"foo": "bar"}, status_code=200)
    else:
        return MockResponse(json_data=None, status_code=404)


class TestMercadoBitcoinApi:
    @patch("requests.get")
    @patch("A005.mercado_bitcoin.apis.MercadoBitcoinApi._get_endpoint", return_value="valid_endpoint")
    def test_get_data_requests_is_called(self, mock_get_endpoint, mock_requests, fix_mercado_bitcoin_api):
        fix_mercado_bitcoin_api.get_data()
        mock_requests.assert_called_once_with("valid_endpoint")

    @patch("requests.get", side_effect=mocked_requests_get)
    @patch("A005.mercado_bitcoin.apis.MercadoBitcoinApi._get_endpoint", return_value="valid_endpoint")
    def test_get_data_with_valid_endpoint(self, mock_get_endpoint, mock_requests, fix_mercado_bitcoin_api):
        actual = fix_mercado_bitcoin_api.get_data()
        excepted = {"foo": "bar"}
        assert actual == excepted

    @patch("requests.get", side_effect=mocked_requests_get)
    @patch("A005.mercado_bitcoin.apis.MercadoBitcoinApi._get_endpoint", return_value="invalid_endpoint")
    def test_get_data_with_valid_endpoint(self, mock_get_endpoint, mock_requests, fix_mercado_bitcoin_api):
        with pytest.raises(Exception):
            fix_mercado_bitcoin_api.get_data()
