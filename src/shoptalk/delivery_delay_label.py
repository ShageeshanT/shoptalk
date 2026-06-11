"""Small seller-facing helper for delivery delay label."""

from __future__ import annotations


def classify_delivery_delay(minutes_late: int | float | bool) -> str:
    """Return a compact dashboard label for delivery delay label."""
    return "On time" if minutes_late <= 0 else "Late" if minutes_late <= 60 else "Critical"
