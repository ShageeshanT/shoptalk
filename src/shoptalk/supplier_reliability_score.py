from __future__ import annotations

def supplier_reliability_score(on_time_batches: int, delayed_batches: int, quality_issues: int) -> int:
    raw_score = on_time_batches * 8 - delayed_batches * 10 - quality_issues * 7
    return max(0, min(100, int(raw_score)))
