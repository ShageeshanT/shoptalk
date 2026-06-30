from __future__ import annotations

def delivery_risk_label(distance_km: float, rain_expected: bool = False) -> str:
    if rain_expected and distance_km > 5: return "high"
    if distance_km > 12: return "medium"
    return "low"
