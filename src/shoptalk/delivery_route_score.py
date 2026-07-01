from __future__ import annotations


def delivery_route_score(stops_count, late_stops, fragile_orders) -> int:
    score = min(stops_count * 4, 32)
    score += min(late_stops * 18, 36)
    score += min(fragile_orders * 10, 30)
    return min(score, 100)
