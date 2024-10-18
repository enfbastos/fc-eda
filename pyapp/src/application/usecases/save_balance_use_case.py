from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from src.application import schemas
from src.application.repositories import BalanceRepository
from src.application.usecases.base import UseCase
from src.domain import Balance
from src.infra.containers import Container


class SaveBalanceUseCase(UseCase):

    @inject
    def __init__(
        self,
        balance_repository: BalanceRepository = Depends(
            Provide[Container.balance_repository]
        )
    ):
        self.balance_repository = balance_repository

    async def execute(self, input: schemas.SaveBalanceInputDto) -> None:
        balance_from = Balance(
            account_id=input.account_id_from,
            balance=input.balance_account_id_from
        )
        balance_to = Balance(
            account_id=input.account_id_to,
            balance=input.balance_account_id_to
        )
        await self.balance_repository.save(
            balance=balance_from
        )
        await self.balance_repository.save(
            balance=balance_to
        )
