from __future__ import annotations


def pickup_readiness_score(packed_items, total_items, minutes_until_pickup) -> int:
    if total_items <= 0:
        return 100
    completion = packed_items / total_items
    score = int(completion * 70)
    if minutes_until_pickup >= 60:
        score += 20
    elif minutes_until_pickup >= 15:
        score += 10
    return max(0, min(score, 100))
