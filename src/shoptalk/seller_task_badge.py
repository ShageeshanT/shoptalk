from __future__ import annotations

def seller_task_badge(open_tasks: int) -> str:
    if open_tasks <= 0: return "none"
    if open_tasks <= 3: return "action"
    return "priority"
