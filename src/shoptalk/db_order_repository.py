from sqlalchemy.orm import Session

from shoptalk.db_mappers import order_from_record, order_to_record
from shoptalk.db_models import OrderRecord
from shoptalk.db_order_queries import filter_orders_by_payment_status, filter_orders_by_status
from shoptalk.schemas import Order, OrderCreate


class SqlOrderRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, payload: OrderCreate) -> Order:
        order = Order(**payload.model_dump())
        self.session.add(order_to_record(order))
        self.session.commit()
        return order

    def get(self, order_id) -> Order | None:
        record = self.session.get(OrderRecord, str(order_id))
        return order_from_record(record) if record else None

    def list_for_business(self, business_id) -> list[Order]:
        return self.search_for_business(business_id)

    def search_for_business(self, business_id, status: str | None = None, payment_status: str | None = None) -> list[Order]:
        query = self.session.query(OrderRecord).filter(OrderRecord.business_id == str(business_id))
        query = filter_orders_by_status(query, status)
        query = filter_orders_by_payment_status(query, payment_status)
        records = query.order_by(OrderRecord.created_at.desc()).all()
        return [order_from_record(record) for record in records]
