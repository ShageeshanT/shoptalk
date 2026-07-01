from __future__ import annotations


def inbox_backlog_score(unread_threads, overdue_threads, vip_threads) -> int:
    score = min(unread_threads * 5, 35)
    score += min(overdue_threads * 12, 36)
    score += min(vip_threads * 10, 25)
    return min(score, 100)
