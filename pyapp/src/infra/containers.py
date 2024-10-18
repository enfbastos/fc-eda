from dependency_injector import containers, providers

from src.infra.database import Database
from src.infra.repositories import BalanceRepositoryDatabase
from src.settings import settings


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        packages=[
            "src.application.usecases"
        ]
    )

    config = providers.Configuration()

    database = providers.Singleton(
        Database,
        db_url=settings.database_url
    )
    
    balance_repository = providers.Factory(
        BalanceRepositoryDatabase,
        session_factory=database.provided.session
    )
