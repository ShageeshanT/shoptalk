from shoptalk.enums import OrderStatus
from shoptalk.order_status_label import order_status_label

def test_order_status_label():
    assert order_status_label(OrderStatus.PAYMENT_PENDING) == "Payment Pending"