from __future__ import annotations

def invoice_followup_score(days_overdue: int, invoice_value_band: int, reminders_sent: int) -> int:
    raw_score = days_overdue * 5 + invoice_value_band * 8 + reminders_sent * 3
    return max(0, min(100, int(raw_score)))
