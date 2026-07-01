from __future__ import annotations

def payment_risk_score(days_overdue: int, reminder_count: int, amount_due: float) -> int:
    overdue = min(40, max(0, days_overdue) * 4)
    reminders = min(30, max(0, reminder_count) * 10)
    amount = min(30, int(max(0.0, amount_due) // 2500) * 5)
    return min(100, overdue + reminders + amount)
