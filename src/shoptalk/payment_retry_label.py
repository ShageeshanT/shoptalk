"""Compact seller dashboard helper for payment retry pressure."""

from __future__ import annotations


def classify_payment_retry(attempts: int | float) -> str:
    """Return a short seller-facing label for payment retry pressure."""
    return "No retry" if attempts < 1 else "Retry gently" if attempts < 3 else "Escalate payment"
