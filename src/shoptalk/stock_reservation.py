def stock_reservation_status(requested: int, available: int) -> str:
    if requested <= 0:
        return "invalid_request"
    if available <= 0:
        return "out_of_stock"
    if requested <= available:
        return "reserved"
    return "partial_only"
