"""Empty-state copy for seller alert widgets."""

from __future__ import annotations


def seller_alert_empty_state(total_alerts: int) -> str | None:
    """Return friendly copy when the seller alert queue is empty."""

    if total_alerts > 0:
        return None
    return "No urgent chats right now. Keep selling, tiny chaos goblin contained."
