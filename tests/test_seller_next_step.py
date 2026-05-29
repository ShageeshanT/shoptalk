from uuid import uuid4

from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.schemas import FollowUp, Order
from shoptalk.seller_next_step import seller_next_step


def _order(status: OrderStatus) -> Order:
    return Order(business_id=uuid4(), title="Order", status=status)


def test_seller_next_step_prefers_open_follow_up() -> None:
    business_id = uuid4()
    order = Order(business_id=business_id, title="Cake", status=OrderStatus.PAID)
    follow_up = FollowUp(
        business_id=business_id,
        title="Ask for address",
        status=FollowUpStatus.OPEN,
    )

    assert seller_next_step(order, [follow_up]) == (
        "Complete the open follow-up before moving this order forward."
    )


def test_seller_next_step_maps_order_status() -> None:
    assert seller_next_step(_order(OrderStatus.PAYMENT_PENDING)) == (
        "Follow up politely about the pending payment."
    )
    assert seller_next_step(_order(OrderStatus.READY)) == (
        "Arrange pickup or delivery with the customer."
    )
