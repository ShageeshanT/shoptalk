from __future__ import annotations

def approval_queue_label(count: int) -> str:
    if count <= 0: return "clear"
    if count <= 5: return "light"
    return "busy"
