from __future__ import annotations

from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.schemas import Customer, FollowUp, Order


def customer_risk_flags(
    customer: Customer,
    orders: list[Order],
    follow_ups: list[FollowUp],
) -> list[str]:
    """Highlight seller-facing risks for a customer profile."""
    flags: list[str] = []

    open_followups = [item for item in follow_ups if item.status == FollowUpStatus.OPEN]
    unpaid_orders = [item for item in orders if item.status == OrderStatus.PAYMENT_PENDING]
    active_orders = [
        item
        for item in orders
        if item.status
        in {OrderStatus.NEW_INQUIRY, OrderStatus.CONFIRMED, OrderStatus.PAYMENT_PENDING}
    ]

    if customer.phone is None and customer.email is None:
        flags.append("missing_contact_route")
    if open_followups:
        flags.append("open_follow_up")
    if unpaid_orders:
        flags.append("payment_pending")
    if len(active_orders) >= 2:
        flags.append("multiple_active_orders")
    if not orders:
        flags.append("new_customer")

    return flags
