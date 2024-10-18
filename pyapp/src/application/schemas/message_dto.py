from enum import Enum

from pydantic import BaseModel


class Message(BaseModel):
    Name: str
    Payload: dict


class Topic(str, Enum):
    balances = "balances"
    transactions = "transactions"
