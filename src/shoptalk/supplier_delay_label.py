"""Compact seller dashboard helper for supplier delay risk."""

from __future__ import annotations


def classify_supplier_delay(delay_hours: int | float) -> str:
    """Return a short seller-facing label for supplier delay risk."""
    return "Supplier on time" if delay_hours < 2 else "Supplier watch" if delay_hours < 12 else "Supplier late"
