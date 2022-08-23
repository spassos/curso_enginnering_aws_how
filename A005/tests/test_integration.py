import datetime
import json

from A005.mercado_bitcoin.apis import DaySummaryApi


class TestDaySummary:
    def test_get_data(self):
        actual = DaySummaryApi(coin="BTC").get_data(date=datetime.date(2022, 8, 20))
        excepted = {'date': '2022-08-20', 'opening': 110341.69, 'closing': 110845.62161, 'lowest': 108750,
                    'highest': 111695.92706945, 'volume': '3026316.97820485', 'quantity': '27.38105508', 'amount': 2501,
                    'avg_price': 110525.94464905}
        assert actual == excepted

    def test_get_data_better(self):
        actual = DaySummaryApi(coin="BTC").get_data(date=datetime.date(2022, 8, 20)).get("date")
        excepted = "2022-08-20"
        assert actual == excepted
