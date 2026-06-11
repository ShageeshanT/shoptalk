"""Small seller-facing helper for basket health label."""

from __future__ import annotations


def classify_basket_health(item_count: int | float | bool) -> str:
    """Return a compact dashboard label for basket health label."""
    return "Empty" if item_count <= 0 else "Healthy" if item_count <= 6 else "Review bulk"
