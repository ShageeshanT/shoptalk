def customer_profile_badge(order_count: int, total_spend: float) -> str:
    if order_count >= 10 or total_spend >= 100000:
        return "vip"
    if order_count >= 3 or total_spend >= 25000:
        return "regular"
    if order_count > 0:
        return "new_buyer"
    return "lead"
