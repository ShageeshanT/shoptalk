"""Batch note rendering for seller alerts."""

from __future__ import annotations

from collections.abc import Iterable

from shoptalk.alert_owner_note import alert_owner_note
from shoptalk.seller_alerts import SellerAlert


def alert_batch_notes(alerts: Iterable[SellerAlert]) -> list[str]:
    """Return owner notes for all active seller alerts."""

    return [alert_owner_note(alert) for alert in alerts]
