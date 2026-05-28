"""Customer timeline summary helpers."""

from __future__ import annotations


def timeline_summary(events: list[str], limit: int = 3) -> list[str]:
    """Return the latest visible timeline events."""

    if limit <= 0:
        return []
    return events[-limit:]
