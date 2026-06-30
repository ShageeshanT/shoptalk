"""Compact seller dashboard helper for refund review pressure."""

from __future__ import annotations


def classify_refund_review(risk_score: int | float) -> str:
    """Return a short seller-facing label for refund review pressure."""
    return "Simple refund" if risk_score < 3 else "Review refund" if risk_score < 7 else "Manager review"
