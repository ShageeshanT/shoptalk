"""Compact seller dashboard helper for seller capacity risk."""

from __future__ import annotations


def classify_seller_capacity_risk(open_tasks: int | float) -> str:
    """Return a short seller-facing label for seller capacity risk."""
    return "Capacity fine" if open_tasks < 5 else "Capacity tight" if open_tasks < 12 else "Over capacity"
