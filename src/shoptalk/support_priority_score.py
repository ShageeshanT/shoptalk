from __future__ import annotations

def support_priority_score(open_issues: int, angry_messages: int, vip_customer: int) -> int:
    raw_score = open_issues * 9 + angry_messages * 12 + vip_customer * 10
    return max(0, min(100, int(raw_score)))
