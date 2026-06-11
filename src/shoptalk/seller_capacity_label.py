"""Small seller-facing helper for seller capacity label."""

from __future__ import annotations


def classify_seller_capacity(free_slots: int | float | bool) -> str:
    """Return a compact dashboard label for seller capacity label."""
    return "Full" if free_slots <= 0 else "Limited" if free_slots <= 3 else "Open"
