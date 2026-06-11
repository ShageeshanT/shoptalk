"""Small seller-facing helper for payment followup label."""

from __future__ import annotations


def classify_payment_followup(days_waiting: int | float | bool) -> str:
    """Return a compact dashboard label for payment followup label."""
    return "Fresh" if days_waiting <= 1 else "Nudge" if days_waiting <= 4 else "Escalate"
