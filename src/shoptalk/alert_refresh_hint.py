"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_refresh_hint(has_new_alerts: bool) -> str:
    return "New customer alerts available. Refresh the queue." if has_new_alerts else "Alert queue is up to date."
