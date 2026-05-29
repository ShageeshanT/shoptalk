from __future__ import annotations

from shoptalk.schemas import Order


def payment_prompt(order: Order, *, payment_method: str = "bank transfer") -> str:
    """Build a concise payment instruction draft for seller approval."""
    amount = _format_amount(order.total_amount)
    title = order.title.strip() if order.title else "your order"
    if amount:
        return f"Your {title} is confirmed. Please complete {amount} via {payment_method}."
    return f"Your {title} is confirmed. Please complete payment via {payment_method}."


def _format_amount(amount: float | None) -> str | None:
    if amount is None:
        return None
    if amount.is_integer():
        return f"Rs {int(amount):,}"
    return f"Rs {amount:,.2f}"
