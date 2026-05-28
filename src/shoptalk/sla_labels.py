"""SLA label helpers for response timing."""

from __future__ import annotations


def sla_label(minutes_waiting: int) -> str:
    """Classify how long a customer has waited."""

    if minutes_waiting >= 240:
        return "overdue"
    if minutes_waiting >= 60:
        return "waiting"
    return "fresh"
