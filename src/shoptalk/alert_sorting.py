"""Sorting helpers for seller alerts."""

from __future__ import annotations

from shoptalk.alert_priority_score import alert_priority_score
from shoptalk.seller_alerts import SellerAlert


def sort_alerts_by_priority(alerts: list[SellerAlert], minutes_waiting: int = 0) -> list[SellerAlert]:
    """Return alerts sorted from highest to lowest action priority."""

    return sorted(alerts, key=lambda alert: alert_priority_score(alert, minutes_waiting), reverse=True)
