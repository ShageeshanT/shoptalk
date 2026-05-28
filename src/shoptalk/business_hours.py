"""Business hour helpers for seller availability."""

from __future__ import annotations


def is_business_hour(hour: int, opens_at: int = 9, closes_at: int = 18) -> bool:
    """Return whether an hour falls inside configured business hours."""

    return opens_at <= hour < closes_at


def availability_label(hour: int) -> str:
    """Return a compact availability label."""

    return "open" if is_business_hour(hour) else "after_hours"
