from __future__ import annotations


def promo_fatigue_score(promos_sent_week, clicks, orders) -> int:
    score = min(promos_sent_week * 12, 60)
    if clicks == 0:
        score += 20
    if orders == 0:
        score += 20
    return min(score, 100)
