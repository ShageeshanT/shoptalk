from __future__ import annotations

def seller_attention_score(unread: int, overdue_followups: int) -> int:
    return max(0, unread) + max(0, overdue_followups) * 3
