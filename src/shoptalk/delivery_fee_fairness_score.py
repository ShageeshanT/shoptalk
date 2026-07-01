from __future__ import annotations

def delivery_fee_fairness_score(distance_km: int, fee_band: int, repeat_customer: int) -> int:
    raw_score = 100 - distance_km * 2 - fee_band * 6 + repeat_customer * 5
    return max(0, min(100, int(raw_score)))
