from __future__ import annotations


def delivery_fee_risk_score(delivery_fee, order_value, customer_queried) -> int:
    ratio = delivery_fee / order_value if order_value else 1
    score = 0
    if ratio >= 0.25:
        score += 45
    elif ratio >= 0.1:
        score += 20
    if customer_queried:
        score += 25
    return min(score, 100)
