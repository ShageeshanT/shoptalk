"""Small seller-facing helper for delivery route label."""

from __future__ import annotations


def classify_delivery_route(stops: int | float | bool) -> str:
    """Return a compact dashboard label for delivery route label."""
    return "Direct" if stops <= 1 else "Route" if stops <= 5 else "Batch"
