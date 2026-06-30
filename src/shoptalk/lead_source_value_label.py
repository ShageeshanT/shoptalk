"""Compact seller dashboard helper for lead source value."""

from __future__ import annotations


def classify_lead_source_value(conversion_percent: int | float) -> str:
    """Return a short seller-facing label for lead source value."""
    return "Weak source" if conversion_percent < 10 else "Promising source" if conversion_percent < 30 else "Strong source"
