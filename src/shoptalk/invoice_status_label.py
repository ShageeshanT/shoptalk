"""Small seller-facing helper for invoice status label."""

from __future__ import annotations


def classify_invoice_status(days_due: int | float | bool) -> str:
    """Return a compact dashboard label for invoice status label."""
    return "Paid" if days_due < 0 else "Due soon" if days_due <= 3 else "Overdue"
