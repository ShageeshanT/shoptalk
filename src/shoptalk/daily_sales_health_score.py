from __future__ import annotations

def daily_sales_health_score(orders_today: int, paid_orders: int, cancelled_orders: int) -> int:
    raw_score = orders_today * 5 + paid_orders * 7 - cancelled_orders * 12
    return max(0, min(100, int(raw_score)))
