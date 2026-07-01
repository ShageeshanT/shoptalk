from __future__ import annotations

def order_profitability_score(margin_band: int, discount_band: int, delivery_cost_band: int) -> int:
    raw_score = margin_band * 10 - discount_band * 5 - delivery_cost_band * 4
    return max(0, min(100, int(raw_score)))
