from __future__ import annotations


def cod_confirm_score(order_value, hours_until_delivery, confirmed) -> int:
    if confirmed:
        return 0
    score = 15
    if order_value >= 30000:
        score += 35
    elif order_value >= 5000:
        score += 15
    if hours_until_delivery <= 6:
        score += 35
    elif hours_until_delivery <= 24:
        score += 15
    return min(score, 100)
