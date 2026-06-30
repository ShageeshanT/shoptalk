def customer_reorder_hint(days_since_last_order):
    return "too_soon" if days_since_last_order < 7 else "good_time" if days_since_last_order <= 45 else "winback"
