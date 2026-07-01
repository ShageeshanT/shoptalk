from __future__ import annotations

def stock_health_score(available_units: int, reserved_units: int, low_stock_alerts: int) -> int:
    raw_score = available_units * 3 - reserved_units * 2 - low_stock_alerts * 10
    return max(0, min(100, int(raw_score)))
