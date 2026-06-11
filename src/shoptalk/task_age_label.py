"""Small seller-facing helper for task age label."""

from __future__ import annotations


def classify_task_age(hours_open: int | float | bool) -> str:
    """Return a compact dashboard label for task age label."""
    return "New" if hours_open <= 2 else "Open" if hours_open <= 24 else "Stale"
