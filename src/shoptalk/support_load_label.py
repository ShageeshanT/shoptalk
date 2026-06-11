"""Small seller-facing helper for support load label."""

from __future__ import annotations


def classify_support_load(tickets: int | float | bool) -> str:
    """Return a compact dashboard label for support load label."""
    return "Clear" if tickets <= 0 else "Normal" if tickets <= 5 else "Heavy"
