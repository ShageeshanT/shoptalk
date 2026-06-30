from __future__ import annotations

def customer_tag_suggestor(total_orders: int) -> str:
    if total_orders >= 10: return "vip"
    if total_orders >= 2: return "repeat"
    return "new"
