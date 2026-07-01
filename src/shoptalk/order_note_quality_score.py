from __future__ import annotations


def order_note_quality_score(has_size, has_color, has_quantity, has_delivery_note, has_customer_note) -> int:
    checks = (has_size, has_color, has_quantity, has_delivery_note, has_customer_note)
    return min(sum(20 for check in checks if check), 100)
