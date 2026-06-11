"""Small seller-facing helper for reply clarity label."""

from __future__ import annotations


def classify_reply_clarity(word_count: int | float | bool) -> str:
    """Return a compact dashboard label for reply clarity label."""
    return "Too short" if word_count < 3 else "Clear" if word_count <= 40 else "Too long"
