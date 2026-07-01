from __future__ import annotations

def customer_engagement_score(recent_replies: int, repeat_orders: int, days_inactive: int) -> int:
    raw_score = recent_replies * 7 + repeat_orders * 9 - days_inactive * 2
    return max(0, min(100, int(raw_score)))
