def order_quantity_label(quantity):
    return "single" if quantity == 1 else "small_batch" if quantity <= 5 else "bulk"
