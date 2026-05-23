from uuid import uuid4

from shoptalk.db_order_repository import SqlOrderRepository
from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.schemas import OrderCreate


def test_sql_order_repository_lists_orders_by_business():
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    session = create_session_factory(engine)()
    repo = SqlOrderRepository(session)
    business_id = uuid4()
    order = repo.create(OrderCreate(business_id=business_id, title="Cupcake box"))
    assert repo.get(order.id).title == "Cupcake box"
    assert [item.id for item in repo.list_for_business(business_id)] == [order.id]
    session.close()
