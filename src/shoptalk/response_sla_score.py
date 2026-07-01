from __future__ import annotations

def response_sla_score(minutes_waiting: int, vip_customer: int, business_hours: int) -> int:
    raw_score = 100 - minutes_waiting + vip_customer * 10 + business_hours * 5
    return max(0, min(100, int(raw_score)))
