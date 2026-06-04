def seller_focus_score(unread: int, overdue: int, high_value_orders: int) -> int:
    score = unread + overdue * 3 + high_value_orders * 2
    return max(0, min(score, 100))
