from __future__ import annotations


def quote_staleness_score(quote_age_hours, price_changed, customer_replied) -> int:
    score = 0
    if quote_age_hours >= 72:
        score += 45
    elif quote_age_hours >= 24:
        score += 25
    if price_changed:
        score += 30
    if customer_replied:
        score -= 20
    return max(0, min(score, 100))
