"""Compact seller dashboard helper for customer note freshness."""

from __future__ import annotations


def classify_customer_note_freshness(days_old: int | float) -> str:
    """Return a short seller-facing label for customer note freshness."""
    return "Fresh note" if days_old < 14 else "Review note" if days_old < 45 else "Stale note"
