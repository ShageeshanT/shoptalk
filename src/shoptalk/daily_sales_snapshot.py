def daily_sales_snapshot(revenue: float, paid_orders: int, pending_orders: int) -> dict[str, float | int | str]:
    status = "quiet"
    if revenue > 0 or paid_orders > 0:
        status = "active"
    if pending_orders > paid_orders:
        status = "needs_collection"
    return {"revenue": round(revenue, 2), "paid_orders": paid_orders, "pending_orders": pending_orders, "status": status}
