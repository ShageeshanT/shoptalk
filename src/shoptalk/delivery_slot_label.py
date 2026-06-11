"""Small seller-facing helper for delivery slot label."""

from __future__ import annotations


def classify_delivery_slot(slots: int | float | bool) -> str:
    """Return a compact dashboard label for delivery slot label."""
    return "Full" if slots <= 0 else "Limited" if slots <= 2 else "Available"
