from __future__ import annotations


def packing_delay_score(items_count, minutes_until_pickup, packed) -> int:
    if packed:
        return 0
    score = 10
    if items_count >= 10:
        score += 25
    elif items_count >= 4:
        score += 15
    if minutes_until_pickup <= 30:
        score += 45
    elif minutes_until_pickup <= 120:
        score += 25
    return min(score, 100)
