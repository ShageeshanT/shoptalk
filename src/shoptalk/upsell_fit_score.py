from __future__ import annotations


def upsell_fit_score(order_total: float, repeat_customer: bool = False, item_count: int = 0) -> int:
    score = 10
    if order_total >= 10000:
        score += 35
    elif order_total >= 3000:
        score += 20
    if repeat_customer:
        score += 25
    if item_count >= 3:
        score += 15
    return min(score, 100)
