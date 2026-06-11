"""Small seller-facing helper for handoff priority label."""

from __future__ import annotations


def classify_handoff_priority(severity: int | float | bool) -> str:
    """Return a compact dashboard label for handoff priority label."""
    return "Normal" if severity < 3 else "Important" if severity < 7 else "Urgent"
