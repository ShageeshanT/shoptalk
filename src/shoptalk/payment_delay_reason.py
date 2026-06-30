def payment_delay_reason(days):
    return "due_today" if days <= 0 else "recent" if days <= 2 else "overdue"
