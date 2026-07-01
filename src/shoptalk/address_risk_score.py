from __future__ import annotations


def address_risk_score(missing_fields, previous_failed_deliveries, map_pin_shared) -> int:
    score = min(missing_fields * 18, 54)
    score += min(previous_failed_deliveries * 15, 30)
    if not map_pin_shared:
        score += 15
    return min(score, 100)
