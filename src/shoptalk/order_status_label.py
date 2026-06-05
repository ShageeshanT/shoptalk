from __future__ import annotations

def order_status_label(status):
    return str(status).replace("_", " ").title()