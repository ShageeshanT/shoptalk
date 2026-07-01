from __future__ import annotations

def inventory_risk_score(stock_on_hand: int, reserved_units: int, daily_sales_rate: float) -> int:
    available = max(0, stock_on_hand - reserved_units)
    if daily_sales_rate <= 0:
        return 0 if available > 0 else 80
    days_left = available / daily_sales_rate
    if days_left <= 1:
        return 95
    if days_left <= 3:
        return 70
    if days_left <= 7:
        return 35
    return 10
