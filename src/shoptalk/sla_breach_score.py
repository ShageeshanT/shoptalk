from __future__ import annotations


def sla_breach_score(minutes_over_sla, customer_value_tier, escalated) -> int:
    score = 0
    if minutes_over_sla >= 120:
        score += 45
    elif minutes_over_sla > 0:
        score += 25
    if customer_value_tier >= 3:
        score += 25
    if escalated:
        score += 20
    return min(score, 100)
