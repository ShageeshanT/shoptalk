from __future__ import annotations


def order_exception_score(missing_items, payment_issue, delivery_issue) -> int:
    score = min(missing_items * 18, 54)
    if payment_issue:
        score += 22
    if delivery_issue:
        score += 22
    return min(score, 100)
