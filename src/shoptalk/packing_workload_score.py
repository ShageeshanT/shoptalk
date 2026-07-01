from __future__ import annotations


def packing_workload_score(open_orders: int, fragile_orders: int = 0, rush_orders: int = 0) -> int:
    score = open_orders * 6 + fragile_orders * 8 + rush_orders * 12
    return max(0, min(score, 100))
