"""Priority scoring for seller alerts."""

from __future__ import annotations

from shoptalk.seller_alerts import SellerAlert

_LEVEL_POINTS = {"danger": 80, "warning": 50, "info": 20}


def alert_priority_score(alert: SellerAlert | None, minutes_waiting: int = 0) -> int:
    """Return a bounded priority score for ordering seller alerts."""

    if alert is None:
        return 0
    wait_points = max(0, minutes_waiting) // 10
    return min(100, _LEVEL_POINTS.get(alert.level, 10) + wait_points)
