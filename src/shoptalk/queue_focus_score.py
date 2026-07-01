from __future__ import annotations

def queue_focus_score(unread_threads: int, vip_threads: int, stale_threads: int) -> int:
    raw_score = unread_threads * 4 + vip_threads * 10 + stale_threads * 7
    return max(0, min(100, int(raw_score)))
