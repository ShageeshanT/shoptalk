"""Compact seller dashboard helper for order margin quality."""

from __future__ import annotations


def classify_order_margin(margin_percent: int | float) -> str:
    """Return a short seller-facing label for order margin quality."""
    return "Thin margin" if margin_percent < 10 else "Healthy margin" if margin_percent < 30 else "Great margin"
