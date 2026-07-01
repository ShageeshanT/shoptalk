"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_acknowledgement_copy(level: str) -> str:
    return "Danger alert acknowledged." if level == "danger" else "Alert acknowledged."
