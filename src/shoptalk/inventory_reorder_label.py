"""Compact seller dashboard helper for inventory reorder urgency."""

from __future__ import annotations


def classify_inventory_reorder(days_left: int | float) -> str:
    """Return a short seller-facing label for inventory reorder urgency."""
    return "Reorder now" if days_left <= 2 else "Reorder soon" if days_left <= 7 else "Stock safe"
