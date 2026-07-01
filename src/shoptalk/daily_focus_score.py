from __future__ import annotations


def daily_focus_score(urgent_orders, overdue_followups, cash_blockers) -> int:
    score = min(urgent_orders * 12, 36)
    score += min(overdue_followups * 10, 30)
    score += min(cash_blockers * 14, 28)
    return min(score, 100)
