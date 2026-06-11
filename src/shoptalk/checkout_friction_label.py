"""Small seller-facing helper for checkout friction label."""

from __future__ import annotations


def classify_checkout_friction(missing_fields: int | float | bool) -> str:
    """Return a compact dashboard label for checkout friction label."""
    return "Smooth" if missing_fields <= 0 else "Needs info" if missing_fields <= 2 else "Blocked"
