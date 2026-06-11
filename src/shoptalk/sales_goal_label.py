"""Small seller-facing helper for sales goal label."""

from __future__ import annotations


def classify_sales_goal(percent: int | float | bool) -> str:
    """Return a compact dashboard label for sales goal label."""
    return "Behind" if percent < 50 else "Tracking" if percent < 100 else "Hit"
