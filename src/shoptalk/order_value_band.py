def order_value_band(amount):
    return "low" if amount < 2500 else "medium" if amount < 10000 else "high"
