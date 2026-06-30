"""Compact seller dashboard helper for quote follow-up timing."""

from __future__ import annotations


def classify_quote_followup(hours_waiting: int | float) -> str:
    """Return a short seller-facing label for quote follow-up timing."""
    return "Fresh quote" if hours_waiting < 6 else "Follow up soon" if hours_waiting < 24 else "Quote going cold"
