from shoptalk.db_health import database_health
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database


def test_database_health_runs_select_one():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    assert database_health(session) == {"database": "ok"}
    session.close()
