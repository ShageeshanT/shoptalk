"""Small seller-facing helper for followup window label."""

from __future__ import annotations


def classify_followup_window(hours_until: int | float | bool) -> str:
    """Return a compact dashboard label for followup window label."""
    return "Overdue" if hours_until < 0 else "Soon" if hours_until <= 6 else "Later"
