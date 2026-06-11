"""Small seller-facing helper for thread summary label."""

from __future__ import annotations


def classify_thread_summary(sentences: int | float | bool) -> str:
    """Return a compact dashboard label for thread summary label."""
    return "Missing" if sentences <= 0 else "Short" if sentences <= 3 else "Detailed"
