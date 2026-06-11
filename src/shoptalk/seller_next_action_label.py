"""Small seller-facing helper for seller next action label."""

from __future__ import annotations


def classify_seller_next_action(priority: int | float | bool) -> str:
    """Return a compact dashboard label for seller next action label."""
    return "Later" if priority < 3 else "Today" if priority < 7 else "Now"
