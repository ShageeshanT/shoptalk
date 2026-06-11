"""Small seller-facing helper for customer value tier."""

from __future__ import annotations


def classify_customer_value_tier(spend: int | float | bool) -> str:
    """Return a compact dashboard label for customer value tier."""
    return "Starter" if spend < 5000 else "Growth" if spend < 25000 else "VIP"
