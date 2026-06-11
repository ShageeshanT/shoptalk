"""Small seller-facing helper for customer patience label."""

from __future__ import annotations


def classify_customer_patience(wait_minutes: int | float | bool) -> str:
    """Return a compact dashboard label for customer patience label."""
    return "Fresh" if wait_minutes <= 15 else "Waiting" if wait_minutes <= 90 else "At risk"
