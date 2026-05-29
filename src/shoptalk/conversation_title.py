from __future__ import annotations

from shoptalk.schemas import Customer, Order


def conversation_title(customer: Customer | None, latest_order: Order | None = None) -> str:
    """Create a compact title for dashboard conversation rows."""
    customer_name = customer.name.strip() if customer and customer.name else "Unknown customer"
    if latest_order and latest_order.title:
        return f"{customer_name} · {latest_order.title.strip()}"
    if customer and customer.channel:
        return f"{customer_name} · {customer.channel}"
    return customer_name


def truncate_conversation_title(title: str, limit: int = 64) -> str:
    if len(title) <= limit:
        return title
    return f"{title[: limit - 1].rstrip()}…"
