"""Small seller-facing helper for refund priority label."""

from __future__ import annotations


def classify_refund_priority(days_open: int | float | bool) -> str:
    """Return a compact dashboard label for refund priority label."""
    return "New" if days_open <= 1 else "Review" if days_open <= 5 else "Escalate"
