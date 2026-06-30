"""Compact seller dashboard helper for daily cashflow health."""

from __future__ import annotations


def classify_daily_cashflow(paid_percent: int | float) -> str:
    """Return a short seller-facing label for daily cashflow health."""
    return "Cashflow weak" if paid_percent < 40 else "Cashflow steady" if paid_percent < 75 else "Cashflow strong"
