"""Small seller-facing helper for order edit label."""

from __future__ import annotations


def classify_order_edit(edits: int | float | bool) -> str:
    """Return a compact dashboard label for order edit label."""
    return "Stable" if edits <= 0 else "Changed" if edits <= 3 else "Messy"
