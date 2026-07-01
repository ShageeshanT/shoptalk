from __future__ import annotations

def message_actionability_score(has_item: int, has_quantity: int, has_deadline: int) -> int:
    raw_score = has_item * 10 + has_quantity * 8 + has_deadline * 7
    return max(0, min(100, int(raw_score)))
