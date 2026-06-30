from __future__ import annotations

def conversation_health_label(unanswered: int, complaints: int) -> str:
    if complaints > 0: return "recovery"
    if unanswered > 3: return "attention"
    return "healthy"
