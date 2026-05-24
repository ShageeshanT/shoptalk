from uuid import uuid4

from shoptalk.db_customer_repository import SqlCustomerRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import CustomerCreate


def test_sql_customer_repository_searches_business_customers():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlCustomerRepository(session)
    business_id = uuid4()
    repo.create(CustomerCreate(business_id=business_id, name="Ama", phone="0771234567"))
    repo.create(CustomerCreate(business_id=business_id, name="Nimal"))
    assert [customer.name for customer in repo.search_for_business(business_id, term="077")] == ["Ama"]
    session.close()
