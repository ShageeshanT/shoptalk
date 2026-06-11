"""Small seller-facing helper for sales velocity label."""

from __future__ import annotations


def classify_sales_velocity(orders_today: int | float | bool) -> str:
    """Return a compact dashboard label for sales velocity label."""
    return "Quiet" if orders_today <= 0 else "Moving" if orders_today <= 5 else "Hot"
