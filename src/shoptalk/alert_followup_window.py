"""Follow-up timing helpers for seller alerts."""

from __future__ import annotations

from shoptalk.seller_alerts import SellerAlert


def alert_followup_window_minutes(alert: SellerAlert | None) -> int | None:
    """Return when the seller should follow up if a customer goes quiet."""

    if alert is None:
        return None
    if alert.level == "danger":
        return 60
    if alert.level == "warning":
        return 180
    return 1440
