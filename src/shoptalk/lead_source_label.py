"""Small seller-facing helper for lead source label."""

from __future__ import annotations


def classify_lead_source(known: int | float | bool) -> str:
    """Return a compact dashboard label for lead source label."""
    return "Unknown" if not known else "Known"
