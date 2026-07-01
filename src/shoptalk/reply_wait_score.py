from __future__ import annotations


def reply_wait_score(unanswered_minutes, customer_messages, owner_messages) -> int:
    score = 0
    if unanswered_minutes >= 240:
        score += 45
    elif unanswered_minutes >= 60:
        score += 25
    elif unanswered_minutes >= 15:
        score += 10
    score += min(customer_messages * 8, 32)
    score -= min(owner_messages * 12, 24)
    return max(0, min(score, 100))
