from __future__ import annotations


def repeat_buyer_score(orders_count, last_order_days, complaints_count) -> int:
    score = min(orders_count * 12, 60)
    if last_order_days <= 30:
        score += 25
    elif last_order_days <= 90:
        score += 10
    score -= min(complaints_count * 15, 30)
    return max(0, min(score, 100))
