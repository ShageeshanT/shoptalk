"""Small seller-facing helper for channel latency label."""

from __future__ import annotations


def classify_channel_latency(minutes: int | float | bool) -> str:
    """Return a compact dashboard label for channel latency label."""
    return "Live" if minutes <= 5 else "Delayed" if minutes <= 60 else "Dormant"
