"""Small seller-facing helper for bulk order label."""

from __future__ import annotations


def classify_bulk_order(quantity: int | float | bool) -> str:
    """Return a compact dashboard label for bulk order label."""
    return "Retail" if quantity < 10 else "Bulk" if quantity < 50 else "Wholesale"
