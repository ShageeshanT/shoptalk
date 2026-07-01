from __future__ import annotations

def reply_quality_score(clarity: int, friendliness: int, next_step: int) -> int:
    raw_score = clarity * 4 + friendliness * 3 + next_step * 5
    return max(0, min(100, int(raw_score)))
