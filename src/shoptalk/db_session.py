from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from shoptalk.db_models import Base
from shoptalk.db_url import build_sqlite_url, default_database_path


def create_db_engine(database_url: str | None = None):
    url = database_url or build_sqlite_url(default_database_path())
    connect_args = {"check_same_thread": False} if url.startswith("sqlite") else {}
    pool_options = {}
    if url == "sqlite+pysqlite:///:memory:":
        from sqlalchemy.pool import StaticPool

        pool_options["poolclass"] = StaticPool
    return create_engine(url, connect_args=connect_args, **pool_options)


def initialize_database(engine) -> None:
    Base.metadata.create_all(engine)


def create_session_factory(engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def session_scope(factory: sessionmaker[Session]) -> Iterator[Session]:
    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
