from shoptalk.order_packaging_label import label_order_packaging


def test_order_packaging_label():
    assert label_order_packaging(True) == "fragile"
