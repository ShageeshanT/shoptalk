from __future__ import annotations

def payment_status_badge(status: str) -> str:
    normalized = (status or "").strip().lower().replace(" ", "_")
    if normalized == "paid":
        return "Paid"
    if normalized in {"partial", "partially_paid"}:
        return "Partial payment"
    if normalized == "overdue":
        return "Payment overdue"
    if normalized in {"failed", "declined"}:
        return "Payment failed"
    return "Payment pending"
