from __future__ import annotations


def refund_attention_score(refund_amount, days_open, customer_angry) -> int:
    score = 0
    if refund_amount >= 20000:
        score += 35
    elif refund_amount > 0:
        score += 15
    if days_open >= 7:
        score += 35
    elif days_open >= 2:
        score += 20
    if customer_angry:
        score += 25
    return min(score, 100)
