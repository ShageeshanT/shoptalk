"""Dashboard card model for seller alerts."""

from __future__ import annotations

from shoptalk.alert_response_sla import alert_response_sla_minutes
from shoptalk.seller_alert_copy import seller_alert_cta
from shoptalk.seller_alerts import SellerAlert


def alert_dashboard_card(alert: SellerAlert) -> dict[str, int | str | None]:
    """Build a compact dashboard card payload for a seller alert."""

    return {
        "level": alert.level,
        "title": alert.title,
        "message": alert.message,
        "cta": seller_alert_cta(alert),
        "sla_minutes": alert_response_sla_minutes(alert),
    }
