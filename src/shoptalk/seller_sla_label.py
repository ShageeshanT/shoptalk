"""Compact seller dashboard helper for seller SLA urgency."""

from __future__ import annotations


def classify_seller_sla(minutes_overdue: int | float) -> str:
    """Return a short seller-facing label for seller SLA urgency."""
    return "On track" if minutes_overdue < 30 else "Watch" if minutes_overdue < 120 else "Late"
