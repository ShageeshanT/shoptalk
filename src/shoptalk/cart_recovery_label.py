"""Small seller-facing helper for cart recovery label."""

from __future__ import annotations


def classify_cart_recovery(hours_idle: int | float | bool) -> str:
    """Return a compact dashboard label for cart recovery label."""
    return "Active" if hours_idle <= 1 else "Recover" if hours_idle <= 24 else "Lost"
