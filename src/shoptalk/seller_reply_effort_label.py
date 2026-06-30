"""Compact seller dashboard helper for seller reply effort."""

from __future__ import annotations


def classify_seller_reply_effort(draft_words: int | float) -> str:
    """Return a short seller-facing label for seller reply effort."""
    return "Quick reply" if draft_words < 20 else "Normal reply" if draft_words < 60 else "Long reply"
