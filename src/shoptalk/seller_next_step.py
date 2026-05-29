from __future__ import annotations

from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.schemas import FollowUp, Order


def seller_next_step(order: Order, follow_ups: list[FollowUp] | None = None) -> str:
    """Return a single plain-English next step for an order card."""
    follow_ups = follow_ups or []
    if any(item.status == FollowUpStatus.OPEN for item in follow_ups):
        return "Complete the open follow-up before moving this order forward."

    if order.status == OrderStatus.NEW_INQUIRY:
        return "Confirm the customer, product, quantity, and delivery details."
    if order.status == OrderStatus.CONFIRMED:
        return "Send payment instructions or mark the payment status."
    if order.status == OrderStatus.PAYMENT_PENDING:
        return "Follow up politely about the pending payment."
    if order.status == OrderStatus.PAID:
        return "Prepare the order and update the customer with progress."
    if order.status == OrderStatus.PREPARING:
        return "Confirm when the order will be ready."
    if order.status == OrderStatus.READY:
        return "Arrange pickup or delivery with the customer."
    if order.status == OrderStatus.DELIVERED:
        return "Ask for feedback or a repeat order opportunity."
    if order.status == OrderStatus.CANCELLED:
        return "Archive the order unless a recovery message is needed."
    return "Review the order manually."
