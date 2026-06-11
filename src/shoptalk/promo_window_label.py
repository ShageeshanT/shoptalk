"""Small seller-facing helper for promo window label."""

from __future__ import annotations


def classify_promo_window(days_left: int | float | bool) -> str:
    """Return a compact dashboard label for promo window label."""
    return "Expired" if days_left < 0 else "Last call" if days_left <= 2 else "Active"
