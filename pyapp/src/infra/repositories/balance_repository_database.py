from collections.abc import Callable
from contextlib import AbstractContextManager

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from src.application.repositories import BalanceRepository
from src.domain import Balance
from src.infra import models


class BalanceRepositoryDatabase(BalanceRepository):

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory

    async def find(self, account_id: str) -> Balance | None:
        with self.session_factory() as session:
            try:
                db_balance = (
                    session
                    .query(models.Balance)
                    .filter(models.Balance.account_id == account_id)
                    .one()
                )
                return Balance.model_validate(db_balance)
            except NoResultFound:
                return None

    async def save(self, balance: Balance) -> None:
        with self.session_factory() as session:
            data = balance.model_dump(exclude_unset=True)
            db_balance = models.Balance(
                **data
            )
            session.merge(db_balance)
            session.flush()
