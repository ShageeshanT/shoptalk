"""Small seller-facing helper for customer question label."""

from __future__ import annotations


def classify_customer_question(questions: int | float | bool) -> str:
    """Return a compact dashboard label for customer question label."""
    return "None" if questions <= 0 else "Simple" if questions <= 2 else "Many"
