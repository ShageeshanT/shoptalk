"""Small seller-facing helper for customer profile depth label."""

from __future__ import annotations


def classify_customer_profile_depth(fields: int | float | bool) -> str:
    """Return a compact dashboard label for customer profile depth label."""
    return "Thin" if fields < 3 else "Useful" if fields < 7 else "Rich"
