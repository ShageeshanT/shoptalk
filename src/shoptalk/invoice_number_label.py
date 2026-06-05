from __future__ import annotations

def invoice_number_label(number: str | None) -> str:
    return f"Invoice {number}" if number else "No invoice"