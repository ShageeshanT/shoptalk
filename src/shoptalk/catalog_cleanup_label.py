"""Small seller-facing helper for catalog cleanup label."""

from __future__ import annotations


def classify_catalog_cleanup(draft_items: int | float | bool) -> str:
    """Return a compact dashboard label for catalog cleanup label."""
    return "Clean" if draft_items <= 0 else "Review" if draft_items <= 10 else "Messy"
