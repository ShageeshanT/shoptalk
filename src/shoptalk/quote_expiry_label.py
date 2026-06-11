"""Small seller-facing helper for quote expiry label."""

from __future__ import annotations


def classify_quote_expiry(hours_left: int | float | bool) -> str:
    """Return a compact dashboard label for quote expiry label."""
    return "Expired" if hours_left <= 0 else "Soon" if hours_left <= 24 else "Valid"
