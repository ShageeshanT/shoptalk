from shoptalk.inventory_alerts import should_hide_item, stock_alert


def test_stock_alert_levels():
    assert stock_alert(0) == "out_of_stock"
    assert stock_alert(3, reorder_level=5) == "low_stock"
    assert stock_alert(10) == "in_stock"


def test_should_hide_item_respects_backorder():
    assert should_hide_item(0) is True
    assert should_hide_item(0, allow_backorder=True) is False
