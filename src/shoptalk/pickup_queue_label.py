"""Compact seller dashboard helper for pickup queue pressure."""

from __future__ import annotations


def classify_pickup_queue(waiting_orders: int | float) -> str:
    """Return a short seller-facing label for pickup queue pressure."""
    return "Quiet pickup" if waiting_orders < 3 else "Pickup building" if waiting_orders < 8 else "Pickup crowded"
