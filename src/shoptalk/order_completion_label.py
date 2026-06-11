"""Small seller-facing helper for order completion label."""

from __future__ import annotations


def classify_order_completion(percent: int | float | bool) -> str:
    """Return a compact dashboard label for order completion label."""
    return "Started" if percent < 40 else "Halfway" if percent < 90 else "Ready"
