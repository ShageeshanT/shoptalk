from __future__ import annotations

def order_readiness_score(items_confirmed: int, payment_ready: int, delivery_ready: int) -> int:
    raw_score = items_confirmed * 10 + payment_ready * 12 + delivery_ready * 12
    return max(0, min(100, int(raw_score)))
