"""Small seller-facing helper for reply personality label."""

from __future__ import annotations


def classify_reply_personality(emoji_count: int | float | bool) -> str:
    """Return a compact dashboard label for reply personality label."""
    return "Plain" if emoji_count <= 0 else "Friendly" if emoji_count <= 3 else "Too much"
