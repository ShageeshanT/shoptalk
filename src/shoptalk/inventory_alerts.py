def stock_alert(stock_count: int, reorder_level: int = 5) -> str:
    if stock_count <= 0:
        return "out_of_stock"
    if stock_count <= reorder_level:
        return "low_stock"
    return "in_stock"


def should_hide_item(stock_count: int, allow_backorder: bool = False) -> bool:
    return stock_count <= 0 and not allow_backorder
