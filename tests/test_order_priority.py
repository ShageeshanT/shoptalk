from shoptalk.enums import OrderStatus
from shoptalk.order_priority import order_priority


def test_order_priority_marks_overdue_as_urgent():
    assert order_priority(OrderStatus.CONFIRMED, overdue=True) == "urgent"


def test_order_priority_detects_payment_and_fulfillment():
    assert order_priority(OrderStatus.PAYMENT_PENDING) == "payment"
    assert order_priority(OrderStatus.PREPARING, paid=True) == "fulfillment"
