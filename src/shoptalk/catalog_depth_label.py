from __future__ import annotations

def catalog_depth_label(count: int) -> str:
    try:
        value = int(count)
    except (TypeError, ValueError):
        value = 0
    if value >= 100:
        return 'Deep catalog'
    if value >= 25:
        return 'Healthy catalog'
    if value >= 1:
        return 'Starter catalog'
    return 'No catalog'
