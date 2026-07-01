from __future__ import annotations


def customer_save_score(lifetime_orders, complaint_open, days_since_last_reply) -> int:
    score = min(lifetime_orders * 10, 50)
    if complaint_open:
        score += 30
    if days_since_last_reply >= 3:
        score += 20
    elif days_since_last_reply >= 1:
        score += 10
    return min(score, 100)
