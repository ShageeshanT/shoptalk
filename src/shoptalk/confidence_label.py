from __future__ import annotations

def confidence_label(score: float) -> str:
    if score >= .8: return "High confidence"
    if score >= .5: return "Medium confidence"
    return "Low confidence"