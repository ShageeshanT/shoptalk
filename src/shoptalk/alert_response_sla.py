"""SLA helpers for seller alert response urgency."""

from __future__ import annotations

from shoptalk.seller_alerts import SellerAlert


def alert_response_sla_minutes(alert: SellerAlert | None) -> int | None:
    """Return suggested response SLA minutes for an alert level."""

    if alert is None:
        return None
    if alert.level == "danger":
        return 10
    if alert.level == "warning":
        return 30
    return 120
