"""Small seller-facing helper for seller energy label."""

from __future__ import annotations


def classify_seller_energy(open_tasks: int | float | bool) -> str:
    """Return a compact dashboard label for seller energy label."""
    return "Calm" if open_tasks <= 3 else "Focused" if open_tasks <= 9 else "Stretched"
