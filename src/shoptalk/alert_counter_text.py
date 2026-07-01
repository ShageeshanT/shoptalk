"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_counter_text(total: int) -> str:
    return "No active alerts" if total <= 0 else "1 active alert" if total == 1 else f"{total} active alerts"
