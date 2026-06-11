"""Small seller-facing helper for lead response label."""

from __future__ import annotations


def classify_lead_response(minutes: int | float | bool) -> str:
    """Return a compact dashboard label for lead response label."""
    return "Instant" if minutes <= 5 else "Fast" if minutes <= 30 else "Warm" if minutes <= 120 else "Cold"
