"""Small seller-facing helper for cart size label."""

from __future__ import annotations


def classify_cart_size(items: int | float | bool) -> str:
    """Return a compact dashboard label for cart size label."""
    return "Empty" if items <= 0 else "Single" if items == 1 else "Bundle" if items <= 4 else "Bulk"
