from __future__ import annotations

def delivery_success_score(on_time_deliveries: int, failed_deliveries: int, address_issues: int) -> int:
    raw_score = on_time_deliveries * 10 - failed_deliveries * 12 - address_issues * 7
    return max(0, min(100, int(raw_score)))
