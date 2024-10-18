import uuid
from datetime import datetime

from pydantic import BaseModel


class GetBalanceByAccountIdInputDto(BaseModel):
    account_id: str

    
class GetBalanceByAccountIdOutputDto(BaseModel):
    account_id: str
    balance: int
    created_at: datetime
    update_at: datetime | None = None
