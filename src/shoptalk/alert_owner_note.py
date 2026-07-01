"""Internal owner notes for seller alerts."""

from __future__ import annotations

from shoptalk.seller_alerts import SellerAlert


def alert_owner_note(alert: SellerAlert | None) -> str:
    """Return a concise internal note for a seller alert."""

    if alert is None:
        return "No alert to review."
    return f"{alert.level.upper()}: {alert.title} - {alert.message}"
