"""Small seller-facing helper for inbox focus label."""

from __future__ import annotations


def classify_inbox_focus(unread: int | float | bool) -> str:
    """Return a compact dashboard label for inbox focus label."""
    return "Clear" if unread <= 0 else "Focus" if unread <= 10 else "Overflow"
