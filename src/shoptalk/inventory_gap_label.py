def inventory_gap_label(requested, available):
    return "covered" if available >= requested else "partial" if available > 0 else "missing"
