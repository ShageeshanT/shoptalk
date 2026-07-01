from __future__ import annotations

def fulfillment_confidence_score(packed_items: int, missing_items: int, rush_orders: int) -> int:
    raw_score = packed_items * 5 - missing_items * 12 - rush_orders * 3
    return max(0, min(100, int(raw_score)))
