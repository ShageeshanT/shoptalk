from __future__ import annotations


def approval_queue_score(drafts_waiting, oldest_wait_minutes, high_value_drafts) -> int:
    score = min(drafts_waiting * 8, 32)
    if oldest_wait_minutes >= 180:
        score += 35
    elif oldest_wait_minutes >= 45:
        score += 20
    score += min(high_value_drafts * 12, 24)
    return min(score, 100)
