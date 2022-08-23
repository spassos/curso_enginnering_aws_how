import datetime
from abc import ABC, abstractmethod
from typing import List

from A005.apis import DaySummaryApi


class DataIngestor(ABC):

    def __init__(self, writer, coins: List[str], default_start_date: datetime.datetime) -> None:
        self.default_start_date = default_start_date
        self.coins = coins
        self.writer = writer
        self.checkpoint = self.load_checkpoint()

    @property
    def checkpoint_filename(self) -> str:
        return f"{self.__class__.__name__}.checkpoint"

    def write_checkpoint(self):
        with open(self.checkpoint_filename, 'w') as f:
            f.write(f"{self.checkpoint}")

    def load_checkpoint(self) -> datetime.date:
        try:
            with open(self.checkpoint_filename, 'r') as f:
                return datetime.datetime.strptime(f.read(), '%Y-%m-%d').date()
        except FileNotFoundError:
            return self.default_start_date

    def _get_checkpoint(self):
        if not self.checkpoint:
            return self.default_start_date
        else:
            return self.checkpoint

    def update_checkpoint(self, value):
        self.checkpoint = value
        self.write_checkpoint()

    @abstractmethod
    def ingest(self) -> None:
        pass


class DaySummaryIngestor(DataIngestor):

    def ingest(self) -> None:
        date = self._get_checkpoint()
        if date < datetime.date.today():
            for coin in self.coins:
                api = DaySummaryApi(coin=coin)
                data = api.get_data(date=date)
                self.writer(coin=coin, api=api.type).write(data)
            self.update_checkpoint(date + datetime.timedelta(days=1))
