"""Compact seller dashboard helper for upsell window."""

from __future__ import annotations


def classify_upsell_window(cart_value: int | float) -> str:
    """Return a short seller-facing label for upsell window."""
    return "No upsell" if cart_value < 2500 else "Soft upsell" if cart_value < 7500 else "Prime upsell"
