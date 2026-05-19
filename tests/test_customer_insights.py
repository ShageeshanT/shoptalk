from uuid import uuid4

from shoptalk.customer_insights import build_customer_insight
from shoptalk.enums import MessageDirection, OrderStatus
from shoptalk.schemas import ConversationMessageOut, FollowUp, Order


def test_customer_insight_summarizes_orders_messages_and_followups() -> None:
    business_id = uuid4()
    customer_id = uuid4()
    insight = build_customer_insight(
        customer_id=customer_id,
        orders=[
            Order(
                business_id=business_id,
                customer_id=customer_id,
                title="Cake",
                status=OrderStatus.PAID,
                total_amount=4200,
            ),
            Order(
                business_id=business_id,
                customer_id=customer_id,
                title="Old cake",
                status=OrderStatus.DELIVERED,
                total_amount=3000,
            ),
        ],
        messages=[
            ConversationMessageOut(
                business_id=business_id,
                customer_id=customer_id,
                sender=MessageDirection.CUSTOMER,
                text="Can I order a cake?",
            )
        ],
        follow_ups=[FollowUp(business_id=business_id, customer_id=customer_id, title="Send menu")],
    )

    assert insight.total_orders == 2
    assert insight.active_orders == 1
    assert insight.delivered_orders == 1
    assert insight.total_spend == 7200
    assert insight.inbound_messages == 1
    assert insight.pending_follow_ups == 1
    assert insight.latest_message_at is not None
