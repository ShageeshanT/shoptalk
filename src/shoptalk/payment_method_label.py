"""Small seller-facing helper for payment method label."""

from __future__ import annotations


def classify_payment_method(is_digital: int | float | bool) -> str:
    """Return a compact dashboard label for payment method label."""
    return "Manual" if not is_digital else "Digital"
