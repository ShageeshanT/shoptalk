"""Compact seller dashboard helper for stock reservation risk."""

from __future__ import annotations


def classify_stock_reserve_risk(reserved_units: int | float) -> str:
    """Return a short seller-facing label for stock reservation risk."""
    return "Low reserve" if reserved_units < 5 else "Reserve watch" if reserved_units < 15 else "Reserve risk"
