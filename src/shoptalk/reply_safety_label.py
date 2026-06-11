"""Small seller-facing helper for reply safety label."""

from __future__ import annotations


def classify_reply_safety(flags: int | float | bool) -> str:
    """Return a compact dashboard label for reply safety label."""
    return "Safe" if flags <= 0 else "Review" if flags <= 2 else "Block"
