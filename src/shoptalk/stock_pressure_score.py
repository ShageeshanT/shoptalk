from __future__ import annotations


def stock_pressure_score(reserved_units, available_units, supplier_delay_days) -> int:
    score = 0
    if available_units <= 0:
        score += 50
    elif reserved_units >= available_units:
        score += 35
    elif reserved_units >= available_units * 0.7:
        score += 20
    if supplier_delay_days >= 3:
        score += 25
    elif supplier_delay_days > 0:
        score += 10
    return min(score, 100)
