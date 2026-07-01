from __future__ import annotations

def payment_collection_score(paid_orders: int, overdue_invoices: int, partial_payments: int) -> int:
    raw_score = paid_orders * 8 + partial_payments * 3 - overdue_invoices * 10
    return max(0, min(100, int(raw_score)))
