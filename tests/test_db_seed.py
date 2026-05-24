from shoptalk.db_seed import ensure_demo_business
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database


def test_ensure_demo_business_is_idempotent():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    first = ensure_demo_business(session)
    second = ensure_demo_business(session)
    assert first.id == second.id
    session.close()
