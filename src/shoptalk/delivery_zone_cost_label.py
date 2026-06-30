"""Compact seller dashboard helper for delivery zone cost."""

from __future__ import annotations


def classify_delivery_zone_cost(distance_km: int | float) -> str:
    """Return a short seller-facing label for delivery zone cost."""
    return "Near zone" if distance_km < 3 else "Standard zone" if distance_km < 10 else "Far zone"
