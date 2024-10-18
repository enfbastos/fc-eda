import logging

from fastapi import Depends, status
from faststream.kafka.fastapi import KafkaRouter
from loguru import logger

from src.application import schemas, usecases
from src.settings import settings

router = KafkaRouter(
    prefix="/balances",
    bootstrap_servers=settings.broker_url,
    logger=logger,
    log_level=logging.DEBUG
)


@router.subscriber(
    schemas.Topic.balances.value,
    group_id=settings.broker_group_id, 
    auto_commit=False
)
async def save_balance(
    message: schemas.Message,
    usecase: usecases.SaveBalanceUseCase = Depends(),
) -> None:
    return await usecase.execute(
        input=schemas.SaveBalanceInputDto(
            account_id_from=message.Payload["account_id_from"],
            account_id_to=message.Payload["account_id_to"],
            balance_account_id_from=message.Payload["balance_account_id_from"],
            balance_account_id_to=message.Payload["balance_account_id_to"]
        )
    )


@router.get(
    "/{account_id}",
    status_code=status.HTTP_200_OK
)
async def get(
    account_id: str,
    usecase: usecases.GetBalanceByAccountIdUseCase = Depends(),
) -> schemas.GetBalanceByAccountIdOutputDto:
    return await usecase.execute(
        input=schemas.GetBalanceByAccountIdInputDto(
            account_id=account_id
        )
    )
