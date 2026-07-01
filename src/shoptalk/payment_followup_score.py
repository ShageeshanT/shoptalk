from __future__ import annotations


def payment_followup_score(amount_due, hours_since_invoice, proof_received) -> int:
    score = 0
    if amount_due >= 25000:
        score += 35
    elif amount_due > 0:
        score += 15
    if hours_since_invoice >= 48:
        score += 35
    elif hours_since_invoice >= 12:
        score += 20
    if proof_received:
        score -= 30
    return max(0, min(score, 100))
