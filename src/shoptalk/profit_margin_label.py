from __future__ import annotations

def profit_margin_label(margin: float | None) -> str:
    if margin is None: return "Margin unknown"
    if margin >= .4: return "Strong margin"
    if margin >= .2: return "Healthy margin"
    return "Thin margin"