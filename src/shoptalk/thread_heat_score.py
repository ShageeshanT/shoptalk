from __future__ import annotations


def thread_heat_score(messages_last_hour, unanswered_minutes, angry_terms) -> int:
    score = min(messages_last_hour * 8, 40)
    if unanswered_minutes >= 60:
        score += 25
    elif unanswered_minutes >= 15:
        score += 10
    score += min(angry_terms * 15, 30)
    return min(score, 100)
