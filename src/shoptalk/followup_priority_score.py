from __future__ import annotations

def followup_priority_score(hours_until_due: int, customer_value: int, pending_questions: int) -> int:
    urgency = 45 if hours_until_due <= 0 else max(0, 45 - hours_until_due * 3)
    value = min(35, max(0, customer_value))
    questions = min(20, max(0, pending_questions) * 5)
    return min(100, urgency + value + questions)
