from uuid import uuid4

from shoptalk.enums import OrderStatus
from shoptalk.order_tags import order_tags
from shoptalk.schemas import Order


def test_order_tags_include_status_value_and_attention() -> None:
    order = Order(
        business_id=uuid4(),
        title="Cake",
        status=OrderStatus.PAYMENT_PENDING,
        total_amount=12000,
    )

    assert order_tags(order) == [
        "payment_pending",
        "value_medium",
        "needs_attention",
        "delivery_unset",
    ]
