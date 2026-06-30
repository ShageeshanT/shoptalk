from __future__ import annotations

def order_deposit_label(total: float, paid: float) -> str:
    if total <= 0: return "no total"
    ratio = paid / total
    if ratio >= 1: return "paid"
    if ratio >= 0.5: return "deposit covered"
    return "deposit needed"
