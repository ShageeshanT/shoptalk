"""Small seller-facing helper for payment confidence label."""

from __future__ import annotations


def classify_payment_confidence(score: int | float | bool) -> str:
    """Return a compact dashboard label for payment confidence label."""
    return "Unclear" if score < 40 else "Likely" if score < 80 else "Confirmed"
