"""Resolution status helpers for seller alerts."""

from __future__ import annotations


def alert_resolution_status(resolved: bool, waiting_on_customer: bool = False) -> str:
    """Return the lifecycle state shown for a seller alert."""

    if resolved:
        return "resolved"
    if waiting_on_customer:
        return "waiting_on_customer"
    return "needs_seller_reply"
