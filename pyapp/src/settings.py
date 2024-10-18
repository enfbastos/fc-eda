from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    service_name: str = "wallet"
    broker_url: str = "localhost:9092"
    broker_group_id: str = "wallet"
    database_url: str = "mysql+pymysql://root:root@localhost:3306/wallet"
    log_level: str = "DEBUG"


settings = Settings()
