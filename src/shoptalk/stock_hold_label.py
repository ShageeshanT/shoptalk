"""Small seller-facing helper for stock hold label."""

from __future__ import annotations


def classify_stock_hold(hours: int | float | bool) -> str:
    """Return a compact dashboard label for stock hold label."""
    return "Fresh" if hours <= 2 else "Held" if hours <= 24 else "Release"
