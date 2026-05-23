from functools import lru_cache

from shoptalk.config import get_settings
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database


@lru_cache
def get_engine():
    settings = get_settings()
    return create_db_engine(settings.database_url)


@lru_cache
def get_session_factory():
    engine = get_engine()
    initialize_database(engine)
    return create_session_factory(engine)


def get_db_session():
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()
