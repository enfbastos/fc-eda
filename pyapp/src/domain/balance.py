from datetime import datetime

from pydantic import BaseModel


class Balance(BaseModel):
    account_id: str
    balance: int
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
