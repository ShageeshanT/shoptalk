"""Small seller-facing helper for address completion label."""

from __future__ import annotations


def classify_address_completion(parts: int | float | bool) -> str:
    """Return a compact dashboard label for address completion label."""
    return "Missing" if parts < 2 else "Partial" if parts < 5 else "Complete"
