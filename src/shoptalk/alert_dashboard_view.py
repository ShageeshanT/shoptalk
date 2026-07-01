"""Presentation view for the seller alert dashboard area."""

from __future__ import annotations

from collections.abc import Iterable

from shoptalk.alert_dashboard_section import alert_dashboard_section
from shoptalk.alert_empty_state import seller_alert_empty_state
from shoptalk.seller_alerts import SellerAlert


def alert_dashboard_view(alerts: Iterable[SellerAlert]) -> dict[str, object]:
    """Build the dashboard section plus empty state copy for the UI."""

    section = alert_dashboard_section(alerts)
    total = int(section["summary"]["total"])
    return {
        **section,
        "empty_state": seller_alert_empty_state(total),
    }
