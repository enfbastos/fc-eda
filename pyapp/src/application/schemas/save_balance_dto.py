from pydantic import BaseModel


class SaveBalanceInputDto(BaseModel):
    account_id_from: str
    account_id_to: str
    balance_account_id_from: int
    balance_account_id_to: int
