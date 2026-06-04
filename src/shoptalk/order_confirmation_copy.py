def order_confirmation_copy(customer_name: str, order_title: str, total: float | None = None) -> str:
    name = customer_name.strip() or "there"
    title = order_title.strip() or "your order"
    if total is None:
        return f"Hi {name}, confirming {title}. We'll update you soon."
    return f"Hi {name}, confirming {title}. Total is Rs {total:,.2f}. We'll update you soon."
