def refund_window_label(days):
    return "open" if days <= 7 else "review" if days <= 14 else "closed"
