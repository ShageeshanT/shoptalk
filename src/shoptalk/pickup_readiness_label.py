"""Small seller-facing helper for pickup readiness label."""

from __future__ import annotations


def classify_pickup_readiness(hours_until: int | float | bool) -> str:
    """Return a compact dashboard label for pickup readiness label."""
    return "Late" if hours_until < 0 else "Soon" if hours_until <= 4 else "Scheduled"
