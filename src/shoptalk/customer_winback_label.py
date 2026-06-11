"""Small seller-facing helper for customer winback label."""

from __future__ import annotations


def classify_customer_winback(days_inactive: int | float | bool) -> str:
    """Return a compact dashboard label for customer winback label."""
    return "Active" if days_inactive <= 14 else "Nudge" if days_inactive <= 45 else "Winback"
