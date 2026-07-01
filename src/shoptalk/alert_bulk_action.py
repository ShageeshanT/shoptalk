"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_bulk_action_label(count: int) -> str:
    return "No alerts selected" if count <= 0 else f"Resolve {count} alert" if count == 1 else f"Resolve {count} alerts"
