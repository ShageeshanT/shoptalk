"""Order flag helpers for operational risk."""

from __future__ import annotations


def order_flags(total: float, same_day: bool, paid: bool) -> list[str]:
    """Return operational flags for an order."""

    flags: list[str] = []
    if same_day:
        flags.append("same_day")
    if total >= 50_000:
        flags.append("high_value")
    if not paid:
        flags.append("payment_pending")
    return flags
