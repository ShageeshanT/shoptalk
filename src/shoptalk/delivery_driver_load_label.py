"""Compact seller dashboard helper for driver delivery load."""

from __future__ import annotations


def classify_delivery_driver_load(stops: int | float) -> str:
    """Return a short seller-facing label for driver delivery load."""
    return "Light route" if stops < 4 else "Normal route" if stops < 9 else "Heavy route"
