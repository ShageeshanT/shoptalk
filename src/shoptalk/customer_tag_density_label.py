"""Small seller-facing helper for customer tag density label."""

from __future__ import annotations


def classify_customer_tag_density(tags: int | float | bool) -> str:
    """Return a compact dashboard label for customer tag density label."""
    return "Untagged" if tags <= 0 else "Tagged" if tags <= 5 else "Crowded"
