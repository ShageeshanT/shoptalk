from shoptalk.inventory_status_badge import inventory_status_badge

def test_inventory_status_badge_thresholds():
    assert inventory_status_badge(0) == "Out of stock"
    assert inventory_status_badge(5) == "Low stock"
    assert inventory_status_badge(20) == "Healthy stock"
    assert inventory_status_badge(60) == "Overstock"
