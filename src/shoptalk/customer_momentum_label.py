"""Small seller-facing helper for customer momentum label."""

from __future__ import annotations


def classify_customer_momentum(touches: int | float | bool) -> str:
    """Return a compact dashboard label for customer momentum label."""
    return "New" if touches <= 1 else "Engaged" if touches <= 4 else "Loyal"
