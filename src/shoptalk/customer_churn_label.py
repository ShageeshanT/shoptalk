"""Small seller-facing helper for customer churn label."""

from __future__ import annotations


def classify_customer_churn(days_since_order: int | float | bool) -> str:
    """Return a compact dashboard label for customer churn label."""
    return "Active" if days_since_order <= 30 else "Cooling" if days_since_order <= 90 else "Churn risk"
