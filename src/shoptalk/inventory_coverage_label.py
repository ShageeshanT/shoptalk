"""Small seller-facing helper for inventory coverage label."""

from __future__ import annotations


def classify_inventory_coverage(days_cover: int | float | bool) -> str:
    """Return a compact dashboard label for inventory coverage label."""
    return "Critical" if days_cover <= 1 else "Low" if days_cover <= 7 else "Covered"
