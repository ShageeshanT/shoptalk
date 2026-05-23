from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.repository_factory import build_sql_repositories


def test_repository_factory_builds_sql_repositories():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repos = build_sql_repositories(session)
    assert repos.businesses is not None
    assert repos.customers is not None
    assert repos.orders is not None
    session.close()
