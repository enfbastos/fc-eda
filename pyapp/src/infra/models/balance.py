from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer

from src.infra.database import Base


class Balance(Base):
    __tablename__ = "balances"
    account_id = Column(String(255), primary_key=True, index=True, unique=True)
    balance = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
