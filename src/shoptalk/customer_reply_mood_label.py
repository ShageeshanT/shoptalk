"""Compact seller dashboard helper for customer reply mood."""

from __future__ import annotations


def classify_customer_reply_mood(sentiment_score: int | float) -> str:
    """Return a short seller-facing label for customer reply mood."""
    return "Tense reply" if sentiment_score < 40 else "Neutral reply" if sentiment_score < 75 else "Warm reply"
