"""Queue labels for active seller alerts."""

from __future__ import annotations


def alert_queue_label(total_alerts: int) -> str:
    """Label the size of the current alert queue."""

    if total_alerts <= 0:
        return "clear"
    if total_alerts <= 2:
        return "watch"
    if total_alerts <= 5:
        return "busy"
    return "overloaded"
