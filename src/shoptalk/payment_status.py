"""Payment status helpers for checkout conversations."""

from __future__ import annotations


def payment_status(total: float, paid: float) -> str:
    """Classify payment completion for an order."""

    if paid <= 0:
        return "unpaid"
    if paid < total:
        return "partial"
    return "paid"


def remaining_balance(total: float, paid: float) -> float:
    """Return a non-negative remaining balance."""

    return max(total - paid, 0.0)
