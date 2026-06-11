"""Small seller-facing helper for order note quality label."""

from __future__ import annotations


def classify_order_note_quality(chars: int | float | bool) -> str:
    """Return a compact dashboard label for order note quality label."""
    return "Missing" if chars <= 0 else "Brief" if chars < 40 else "Detailed"
