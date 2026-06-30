from shoptalk.stock_warning_label import label_stock_warning


def test_stock_warning_label():
    assert label_stock_warning(2) == "low stock"
