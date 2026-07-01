from __future__ import annotations


def lead_decay_score(hours_since_first_message, replies_sent, quoted) -> int:
    score = 0
    if hours_since_first_message >= 72:
        score += 45
    elif hours_since_first_message >= 24:
        score += 25
    elif hours_since_first_message >= 6:
        score += 10
    if replies_sent == 0:
        score += 30
    if not quoted:
        score += 15
    return min(score, 100)
