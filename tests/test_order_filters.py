from uuid import uuid4

from shoptalk.enums import OrderStatus
from shoptalk.order_filters import active_orders, unpaid_orders
from shoptalk.schemas import Order


def test_unpaid_orders_excludes_paid_orders() -> None:
    paid = Order(business_id=uuid4(), title="Paid", payment_status="paid")
    pending = Order(business_id=uuid4(), title="Pending", payment_status="pending")
    assert unpaid_orders([paid, pending]) == [pending]


def test_active_orders_excludes_delivered_and_cancelled() -> None:
    delivered = Order(business_id=uuid4(), title="Done", status=OrderStatus.DELIVERED)
    open_order = Order(business_id=uuid4(), title="Open")
    assert active_orders([delivered, open_order]) == [open_order]
