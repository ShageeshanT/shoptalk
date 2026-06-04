def sales_stage(has_price: bool, has_quantity: bool, has_delivery: bool, paid: bool) -> str:
    if paid:
        return "paid"
    if has_price and has_quantity and has_delivery:
        return "ready_to_confirm"
    if has_price or has_quantity:
        return "qualifying"
    return "new"
