"""Small helper for seller alert UI."""

from __future__ import annotations


def alert_escalation_label(level: str) -> str:
    return "owner_review" if level == "danger" else "seller_queue" if level == "warning" else "normal"
