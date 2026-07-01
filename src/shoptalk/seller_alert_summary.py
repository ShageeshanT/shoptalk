"""Summaries for seller alerts shown in the daily workspace."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable

from shoptalk.seller_alerts import SellerAlert


def summarize_seller_alerts(alerts: Iterable[SellerAlert | None]) -> dict[str, int | str]:
    """Return compact alert counts and the strongest level for a seller view."""

    counts: Counter[str] = Counter(alert.level for alert in alerts if alert is not None)
    total = sum(counts.values())
    if counts.get("danger", 0):
        strongest = "danger"
    elif counts.get("warning", 0):
        strongest = "warning"
    elif total:
        strongest = "info"
    else:
        strongest = "clear"
    return {
        "total": total,
        "danger": counts.get("danger", 0),
        "warning": counts.get("warning", 0),
        "info": counts.get("info", 0),
        "strongest": strongest,
    }
