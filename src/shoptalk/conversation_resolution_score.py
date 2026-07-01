from __future__ import annotations

def conversation_resolution_score(answered_questions: int, open_questions: int, next_step_set: int) -> int:
    raw_score = answered_questions * 7 - open_questions * 5 + next_step_set * 10
    return max(0, min(100, int(raw_score)))
