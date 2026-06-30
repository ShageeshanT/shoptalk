from uuid import uuid4

from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.schemas import FollowUp, Order
from shoptalk.seller_blocker_label import seller_blocker_label


def _order(status: OrderStatus) -> Order:
    return Order(business_id=uuid4(), title="Order", status=status)


def test_seller_blocker_label_prefers_open_followups() -> None:
    business_id = uuid4()
    order = Order(business_id=business_id, title="Cake", status=OrderStatus.PAID)
    follow_up = FollowUp(
        business_id=business_id,
        title="Confirm pickup time",
        status=FollowUpStatus.OPEN,
    )

    assert seller_blocker_label(order, [follow_up]) == "open follow-up blocking progress"


def test_seller_blocker_label_maps_active_statuses() -> None:
    assert seller_blocker_label(_order(OrderStatus.NEW_INQUIRY)) == "details need confirmation"
    assert seller_blocker_label(_order(OrderStatus.PAYMENT_PENDING)) == "payment still pending"
    assert seller_blocker_label(_order(OrderStatus.READY)) == "handoff not arranged"


def test_seller_blocker_label_handles_completed_statuses() -> None:
    assert seller_blocker_label(_order(OrderStatus.DELIVERED)) == "feedback opportunity"
    assert seller_blocker_label(_order(OrderStatus.CANCELLED)) == "cancelled order"
