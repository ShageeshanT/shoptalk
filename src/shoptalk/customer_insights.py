from collections import Counter
from uuid import UUID

from shoptalk.enums import MessageDirection, OrderStatus
from shoptalk.schemas import ConversationMessageOut, CustomerInsight, FollowUp, Order


def build_customer_insight(
    customer_id: UUID,
    orders: list[Order],
    messages: list[ConversationMessageOut],
    follow_ups: list[FollowUp],
) -> CustomerInsight:
    customer_orders = [order for order in orders if order.customer_id == customer_id]
    customer_messages = [message for message in messages if message.customer_id == customer_id]
    customer_follow_ups = [follow_up for follow_up in follow_ups if follow_up.customer_id == customer_id]

    statuses = Counter(order.status for order in customer_orders)
    total_spend = sum(order.total_amount or 0 for order in customer_orders)
    inbound_messages = sum(
        1 for message in customer_messages if message.sender == MessageDirection.CUSTOMER
    )
    latest_message_at = max((message.received_at for message in customer_messages), default=None)

    return CustomerInsight(
        customer_id=customer_id,
        total_orders=len(customer_orders),
        active_orders=sum(
            statuses[status]
            for status in {
                OrderStatus.NEW_INQUIRY,
                OrderStatus.CONFIRMED,
                OrderStatus.PAYMENT_PENDING,
                OrderStatus.PAID,
                OrderStatus.PREPARING,
                OrderStatus.READY,
            }
        ),
        delivered_orders=statuses[OrderStatus.DELIVERED],
        cancelled_orders=statuses[OrderStatus.CANCELLED],
        total_spend=total_spend,
        inbound_messages=inbound_messages,
        pending_follow_ups=len(customer_follow_ups),
        latest_message_at=latest_message_at,
    )
