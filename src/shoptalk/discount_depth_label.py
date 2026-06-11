"""Small seller-facing helper for discount depth label."""

from __future__ import annotations


def classify_discount_depth(percent: int | float | bool) -> str:
    """Return a compact dashboard label for discount depth label."""
    return "None" if percent <= 0 else "Light" if percent <= 10 else "Deep"
