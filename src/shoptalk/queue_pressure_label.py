"""Small seller-facing helper for queue pressure label."""

from __future__ import annotations


def classify_queue_pressure(pending_count: int | float | bool) -> str:
    """Return a compact dashboard label for queue pressure label."""
    return "Clear" if pending_count <= 0 else "Light" if pending_count <= 3 else "Busy" if pending_count <= 8 else "Overloaded"
