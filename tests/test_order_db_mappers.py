from uuid import uuid4

from shoptalk.db_mappers import order_from_record, order_to_record
from shoptalk.enums import OrderStatus
from shoptalk.schemas import Order


def test_order_mapper_preserves_money_status_and_delivery():
    order = Order(
        business_id=uuid4(),
        customer_id=uuid4(),
        title="Chocolate cake",
        status=OrderStatus.CONFIRMED,
        payment_status="deposit_paid",
        total_amount=4500,
        delivery_date="Saturday",
    )
    restored = order_from_record(order_to_record(order))
    assert restored.title == "Chocolate cake"
    assert restored.status == OrderStatus.CONFIRMED
    assert restored.payment_status == "deposit_paid"
    assert restored.total_amount == 4500
    assert restored.delivery_date == "Saturday"
