from __future__ import annotations


def delivery_promise_score(minutes_until_due, has_address, driver_assigned) -> int:
    score = 0
    if minutes_until_due <= 0:
        score += 55
    elif minutes_until_due <= 30:
        score += 35
    elif minutes_until_due <= 120:
        score += 15
    if not has_address:
        score += 25
    if not driver_assigned:
        score += 20
    return min(score, 100)
