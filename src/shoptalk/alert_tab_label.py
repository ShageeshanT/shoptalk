"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_tab_label(total: int) -> str:
    return "Alerts" if total <= 0 else f"Alerts ({total})"
