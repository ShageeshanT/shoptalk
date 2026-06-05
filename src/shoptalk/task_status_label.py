from __future__ import annotations

def task_status_label(done: bool) -> str:
    return "Done" if done else "Open"