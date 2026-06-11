"""Small seller-facing helper for customer temperature label."""

from __future__ import annotations


def classify_customer_temperature(score: int | float | bool) -> str:
    """Return a compact dashboard label for customer temperature label."""
    return "Cold" if score < 35 else "Warm" if score < 75 else "Hot"
