from __future__ import annotations

def handoff_risk_score(missing_context: int, urgent_issue: int, owner_needed: int) -> int:
    raw_score = missing_context * 8 + urgent_issue * 15 + owner_needed * 10
    return max(0, min(100, int(raw_score)))
