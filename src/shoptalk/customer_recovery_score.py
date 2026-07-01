from __future__ import annotations


def customer_recovery_score(days_inactive: int, lifetime_orders: int, last_rating: int | None = None) -> int:
    score = 0
    if days_inactive >= 90:
        score += 45
    elif days_inactive >= 30:
        score += 25
    if lifetime_orders >= 5:
        score += 25
    elif lifetime_orders >= 2:
        score += 10
    if last_rating is not None and last_rating >= 4:
        score += 15
    return min(score, 100)
