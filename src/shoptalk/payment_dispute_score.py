from __future__ import annotations


def payment_dispute_score(amount, days_open, proof_conflict) -> int:
    score = 0
    if amount >= 20000:
        score += 35
    elif amount > 0:
        score += 15
    if days_open >= 5:
        score += 35
    elif days_open >= 1:
        score += 15
    if proof_conflict:
        score += 25
    return min(score, 100)
