"""Small seller-facing helper for thread importance label."""

from __future__ import annotations


def classify_thread_importance(score: int | float | bool) -> str:
    """Return a compact dashboard label for thread importance label."""
    return "Low" if score < 30 else "Medium" if score < 70 else "High"
