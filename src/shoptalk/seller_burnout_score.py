from __future__ import annotations

def seller_burnout_score(open_threads: int, late_orders: int, hours_active: int) -> int:
    raw_score = open_threads * 3 + late_orders * 8 + hours_active * 4
    return max(0, min(100, int(raw_score)))
