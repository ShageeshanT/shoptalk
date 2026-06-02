def conversion_rate(orders: int, inquiries: int) -> float:
    if inquiries <= 0:
        return 0.0
    return round((orders / inquiries) * 100, 2)


def average_order_value(total_revenue: float, order_count: int) -> float:
    if order_count <= 0:
        return 0.0
    return round(total_revenue / order_count, 2)
