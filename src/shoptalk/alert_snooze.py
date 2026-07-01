"""Snooze rules for seller alerts."""

from __future__ import annotations

from shoptalk.seller_alerts import SellerAlert


def can_snooze_alert(alert: SellerAlert | None) -> bool:
    """Return whether a seller alert can be snoozed safely."""

    if alert is None:
        return False
    return alert.level in {"warning", "info"}
