from __future__ import annotations

def catalog_availability_label(active: bool) -> str:
    return "Available" if active else "Hidden"