"""Small seller-facing helper for quote readiness label."""

from __future__ import annotations


def classify_quote_readiness(missing_prices: int | float | bool) -> str:
    """Return a compact dashboard label for quote readiness label."""
    return "Ready" if missing_prices <= 0 else "Review" if missing_prices <= 2 else "Incomplete"
