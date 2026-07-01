from __future__ import annotations


def cart_abandonment_score(minutes_since_reply: int, item_count: int, has_checkout_link: bool) -> int:
    score = 0
    if minutes_since_reply >= 240:
        score += 45
    elif minutes_since_reply >= 60:
        score += 25
    if item_count >= 4:
        score += 20
    elif item_count >= 1:
        score += 10
    if has_checkout_link:
        score += 20
    return min(score, 100)
