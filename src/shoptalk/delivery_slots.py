"""Delivery slot formatting helpers."""

from __future__ import annotations


def format_delivery_slot(day: str, window: str) -> str:
    """Format a day and time window for seller/customer views."""

    return f"{day.strip().title()} · {window.strip()}"


def is_same_day_slot(day: str) -> bool:
    """Return whether a requested slot is for today."""

    return day.strip().lower() in {"today", "tonight"}
