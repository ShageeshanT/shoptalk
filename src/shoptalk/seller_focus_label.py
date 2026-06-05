from __future__ import annotations

def seller_focus_label(score: int) -> str:
    if score >= 80: return "Clear focus"
    if score >= 50: return "Mixed focus"
    return "Needs attention"