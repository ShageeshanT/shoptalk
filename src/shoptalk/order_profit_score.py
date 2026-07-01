from __future__ import annotations


def order_profit_score(revenue, cost, discount) -> int:
    if revenue <= 0:
        return 0
    margin = (revenue - cost - discount) / revenue
    if margin >= 0.35:
        return 90
    if margin >= 0.2:
        return 70
    if margin >= 0.1:
        return 45
    return 20
