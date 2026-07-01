from __future__ import annotations


def cash_collection_score(unpaid_amount: float, invoice_age_days: int, reminders_sent: int = 0) -> int:
    score = 0
    if unpaid_amount >= 50000:
        score += 40
    elif unpaid_amount >= 10000:
        score += 25
    elif unpaid_amount > 0:
        score += 10
    if invoice_age_days >= 14:
        score += 35
    elif invoice_age_days >= 3:
        score += 15
    score += min(reminders_sent * 5, 15)
    return min(score, 100)
