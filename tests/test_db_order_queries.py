from uuid import uuid4

from shoptalk.db_mappers import order_to_record
from shoptalk.db_models import OrderRecord
from shoptalk.db_order_queries import filter_orders_by_payment_status, filter_orders_by_status
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.enums import OrderStatus
from shoptalk.schemas import Order


def test_order_query_filters_by_status_and_payment():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    business_id = uuid4()
    session.add(order_to_record(Order(business_id=business_id, title="Cake", status=OrderStatus.CONFIRMED, payment_status="paid")))
    session.commit()
    query = filter_orders_by_payment_status(filter_orders_by_status(session.query(OrderRecord), "confirmed"), "paid")
    assert query.count() == 1
    session.close()
