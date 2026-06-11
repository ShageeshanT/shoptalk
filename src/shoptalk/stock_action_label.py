"""Small seller-facing helper for stock action label."""

from __future__ import annotations


def classify_stock_action(stock: int | float | bool) -> str:
    """Return a compact dashboard label for stock action label."""
    return "Restock" if stock <= 0 else "Watch" if stock <= 5 else "Healthy"
