"""Small seller-facing helper for customer reply gap label."""

from __future__ import annotations


def classify_customer_reply_gap(hours: int | float | bool) -> str:
    """Return a compact dashboard label for customer reply gap label."""
    return "Recent" if hours <= 2 else "Follow up" if hours <= 48 else "Dormant"
