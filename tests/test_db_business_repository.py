from shoptalk.db_business_repository import SqlBusinessRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import BusinessCreate


def test_sql_business_repository_creates_and_reads_businesses():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlBusinessRepository(session)
    business = repo.create(BusinessCreate(name="Kavi Bakes"))
    assert repo.get(business.id).name == "Kavi Bakes"
    assert repo.list()[0].id == business.id
    session.close()
