from contextlib import contextmanager

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()


class Database:

    def __init__(self, db_url: str, echo: bool = False, max_overflow: int = 10, pool_pre_ping: bool = False, pool_recycle: int = -1, pool_size: int = 5) -> None:
        self._engine = create_engine(
            db_url,
            echo=echo,
            echo_pool=echo,
            max_overflow=max_overflow,
            pool_pre_ping=pool_pre_ping,
            pool_recycle=pool_recycle,
            pool_size=pool_size
        )
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                expire_on_commit=True,
                bind=self._engine,
            ),
        )
        orm.configure_mappers()

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self):
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
        finally:
            session.close()
