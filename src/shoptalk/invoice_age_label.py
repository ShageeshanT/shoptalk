"""Compact seller dashboard helper for invoice age."""

from __future__ import annotations


def classify_invoice_age(days_open: int | float) -> str:
    """Return a short seller-facing label for invoice age."""
    return "Fresh invoice" if days_open < 3 else "Invoice aging" if days_open < 10 else "Invoice overdue"
