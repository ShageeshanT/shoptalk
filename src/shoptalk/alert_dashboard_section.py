"""Dashboard section helpers for seller alerts."""

from __future__ import annotations

from collections.abc import Iterable

from shoptalk.alert_dashboard_card import alert_dashboard_card
from shoptalk.alert_queue_label import alert_queue_label
from shoptalk.alert_sorting import sort_alerts_by_priority
from shoptalk.seller_alert_summary import summarize_seller_alerts
from shoptalk.seller_alerts import SellerAlert


def alert_dashboard_section(alerts: Iterable[SellerAlert]) -> dict[str, object]:
    """Build a complete seller alert section payload."""

    materialized = list(alerts)
    sorted_alerts = sort_alerts_by_priority(materialized)
    summary = summarize_seller_alerts(sorted_alerts)
    return {
        "summary": summary,
        "queue_label": alert_queue_label(int(summary["total"])),
        "cards": [alert_dashboard_card(alert) for alert in sorted_alerts],
    }
