from uuid import uuid4

from shoptalk.db_order_repository import SqlOrderRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.enums import OrderStatus
from shoptalk.schemas import OrderCreate


def test_sql_order_repository_searches_by_status():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlOrderRepository(session)
    business_id = uuid4()
    repo.create(OrderCreate(business_id=business_id, title="Cake", status=OrderStatus.CONFIRMED, payment_status="paid"))
    repo.create(OrderCreate(business_id=business_id, title="Cookies"))
    assert [order.title for order in repo.search_for_business(business_id, status="confirmed")] == ["Cake"]
    session.close()
