from dependency_injector.wiring import Provide, inject
from fastapi import Depends, HTTPException

from src.application import schemas
from src.application.repositories import BalanceRepository
from src.application.usecases.base import UseCase
from src.infra.containers import Container


class GetBalanceByAccountIdUseCase(UseCase):

    @inject
    def __init__(
        self,
        balance_repository: BalanceRepository = Depends(
            Provide[Container.balance_repository]
        )
    ):
        self.balance_repository = balance_repository

    async def execute(self, input: schemas.GetBalanceByAccountIdInputDto) -> schemas.GetBalanceByAccountIdOutputDto:
        result = await self.balance_repository.find(
            account_id=input.account_id
        )
        if not result:
            raise HTTPException(status_code=404)
        return schemas.GetBalanceByAccountIdOutputDto(
            account_id=result.account_id,
            balance=result.balance,
            created_at=result.created_at,
            update_at=result.updated_at
        )
