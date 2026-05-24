from uuid import uuid4

from shoptalk.db_customer_queries import search_customers
from shoptalk.db_mappers import customer_to_record
from shoptalk.db_models import CustomerRecord
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import Customer


def test_search_customers_matches_name_phone_or_email():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    session.add(customer_to_record(Customer(business_id=uuid4(), name="Ama", phone="0771234567", email="ama@example.com")))
    session.commit()
    assert search_customers(session.query(CustomerRecord), "ama").count() == 1
    assert search_customers(session.query(CustomerRecord), "077").count() == 1
    session.close()
