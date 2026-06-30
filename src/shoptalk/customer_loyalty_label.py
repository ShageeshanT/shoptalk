"""Compact seller dashboard helper for customer loyalty tier."""

from __future__ import annotations


def classify_customer_loyalty(orders: int | float) -> str:
    """Return a short seller-facing label for customer loyalty tier."""
    return "New buyer" if orders < 2 else "Returning buyer" if orders < 6 else "Loyal buyer"
