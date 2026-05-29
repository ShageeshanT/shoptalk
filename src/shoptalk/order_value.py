from __future__ import annotations

from shoptalk.schemas import Order


def order_value_band(order: Order) -> str:
    """Classify an order by value so sellers can prioritize important chats."""
    if order.total_amount is None:
        return "unknown"
    if order.total_amount >= 25000:
        return "high"
    if order.total_amount >= 7500:
        return "medium"
    return "low"


def order_value_summary(orders: list[Order]) -> dict[str, int]:
    summary = {"high": 0, "medium": 0, "low": 0, "unknown": 0}
    for order in orders:
        summary[order_value_band(order)] += 1
    return summary
