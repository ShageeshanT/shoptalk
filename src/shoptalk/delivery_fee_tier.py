"""Small seller-facing helper for delivery fee tier."""

from __future__ import annotations


def classify_delivery_fee_tier(fee: int | float | bool) -> str:
    """Return a compact dashboard label for delivery fee tier."""
    return "Free" if fee <= 0 else "Standard" if fee <= 500 else "Premium"
