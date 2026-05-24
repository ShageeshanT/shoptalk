from sqlalchemy.orm import Query

from shoptalk.db_models import OrderRecord


def filter_orders_by_status(query: Query, status: str | None):
    if not status:
        return query
    return query.filter(OrderRecord.status == status)


def filter_orders_by_payment_status(query: Query, payment_status: str | None):
    if not payment_status:
        return query
    return query.filter(OrderRecord.payment_status == payment_status)
