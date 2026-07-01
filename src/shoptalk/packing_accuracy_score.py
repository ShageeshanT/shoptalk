from __future__ import annotations

def packing_accuracy_score(packed_items: int, corrected_items: int, missing_items: int) -> int:
    raw_score = packed_items * 6 - corrected_items * 5 - missing_items * 15
    return max(0, min(100, int(raw_score)))
