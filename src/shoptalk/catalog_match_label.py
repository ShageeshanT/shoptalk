"""Small seller-facing helper for catalog match label."""

from __future__ import annotations


def classify_catalog_match(matches: int | float | bool) -> str:
    """Return a compact dashboard label for catalog match label."""
    return "None" if matches <= 0 else "Possible" if matches == 1 else "Multiple"
