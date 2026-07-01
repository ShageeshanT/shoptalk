"""Digest helpers for seller alerts."""

from __future__ import annotations

from collections.abc import Iterable

from shoptalk.seller_alert_copy import seller_alert_cta
from shoptalk.seller_alerts import SellerAlert
from shoptalk.seller_alert_summary import summarize_seller_alerts


def seller_alert_digest(alerts: Iterable[SellerAlert | None]) -> str:
    """Build a short daily digest line for seller alert widgets."""

    materialized = [alert for alert in alerts if alert is not None]
    summary = summarize_seller_alerts(materialized)
    if summary["total"] == 0:
        return "No active seller alerts."

    first = materialized[0]
    cta = seller_alert_cta(first)
    return f"{summary['total']} active alerts. Strongest: {summary['strongest']}. Next: {cta}"
