from uuid import uuid4

from shoptalk.db_customer_repository import SqlCustomerRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import CustomerCreate


def test_sql_customer_repository_lists_by_business():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlCustomerRepository(session)
    business_id = uuid4()
    other_id = uuid4()
    customer = repo.create(CustomerCreate(business_id=business_id, name="Ama"))
    repo.create(CustomerCreate(business_id=other_id, name="Other"))
    assert [item.id for item in repo.list_for_business(business_id)] == [customer.id]
    session.close()
