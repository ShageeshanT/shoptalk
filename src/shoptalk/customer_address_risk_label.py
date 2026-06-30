"""Compact seller dashboard helper for address completion risk."""

from __future__ import annotations


def classify_customer_address_risk(missing_parts: int | float) -> str:
    """Return a short seller-facing label for address completion risk."""
    return "Address ready" if missing_parts < 1 else "Needs detail" if missing_parts < 3 else "Address risky"
