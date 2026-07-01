from __future__ import annotations

def lead_quality_score(budget_match: int, urgency: int, clear_need: int) -> int:
    raw_score = budget_match * 9 + urgency * 7 + clear_need * 8
    return max(0, min(100, int(raw_score)))
