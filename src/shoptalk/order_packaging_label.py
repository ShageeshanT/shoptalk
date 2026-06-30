"""Compact seller dashboard helper for order packaging workload."""

from __future__ import annotations


def classify_order_packaging(item_count: int | float) -> str:
    """Return a short seller-facing label for order packaging workload."""
    return "Small pack" if item_count < 3 else "Medium pack" if item_count < 10 else "Bulk pack"
