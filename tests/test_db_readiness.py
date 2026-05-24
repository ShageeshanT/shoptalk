from shoptalk.db_readiness import database_readiness
from shoptalk.db_session import create_db_engine, initialize_database


def test_database_readiness_reports_ready_after_init():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    assert database_readiness(engine)["ready"] is True


def test_database_readiness_reports_missing_tables_before_init():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    result = database_readiness(engine)
    assert result["ready"] is False
    assert "businesses" in result["missing_tables"]
