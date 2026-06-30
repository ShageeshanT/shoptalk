from __future__ import annotations

from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.schemas import FollowUp, Order


def seller_blocker_label(order: Order, follow_ups: list[FollowUp] | None = None) -> str:
    """Return a compact blocker label for seller dashboard order cards."""
    follow_ups = follow_ups or []
    open_followups = [item for item in follow_ups if item.status == FollowUpStatus.OPEN]
    if open_followups:
        return "open follow-up blocking progress"

    if order.status == OrderStatus.NEW_INQUIRY:
        return "details need confirmation"
    if order.status == OrderStatus.CONFIRMED:
        return "payment request not sent"
    if order.status == OrderStatus.PAYMENT_PENDING:
        return "payment still pending"
    if order.status == OrderStatus.PAID:
        return "preparation not started"
    if order.status == OrderStatus.PREPARING:
        return "ready time not confirmed"
    if order.status == OrderStatus.READY:
        return "handoff not arranged"
    if order.status == OrderStatus.DELIVERED:
        return "feedback opportunity"
    if order.status == OrderStatus.CANCELLED:
        return "cancelled order"
    return "manual review needed"
