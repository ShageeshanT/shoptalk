from sqlalchemy import inspect

from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database


def test_initialize_database_creates_tables():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    tables = set(inspect(engine).get_table_names())
    assert {"businesses", "customers", "orders"}.issubset(tables)


def test_create_session_factory_returns_sessions():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    factory = create_session_factory(engine)
    session = factory()
    try:
        assert session.bind is engine
    finally:
        session.close()
