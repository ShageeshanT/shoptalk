from __future__ import annotations


def seller_overload_score(open_threads, open_orders, hours_since_break) -> int:
    score = min(open_threads * 4, 32) + min(open_orders * 5, 35)
    if hours_since_break >= 8:
        score += 25
    elif hours_since_break >= 4:
        score += 10
    return min(score, 100)
