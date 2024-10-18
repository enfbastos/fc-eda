import uuid
from abc import ABC, abstractmethod

from src.domain import Balance


class BalanceRepository(ABC):

    @abstractmethod
    async def find(self, account_id: str) -> Balance | None:
        ...

    @abstractmethod
    async def save(self, balance: Balance) -> Balance:
        ...
