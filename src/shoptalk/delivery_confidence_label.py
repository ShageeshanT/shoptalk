"""Small seller-facing helper for delivery confidence label."""

from __future__ import annotations


def classify_delivery_confidence(score: int | float | bool) -> str:
    """Return a compact dashboard label for delivery confidence label."""
    return "Low" if score < 40 else "Medium" if score < 75 else "High"
