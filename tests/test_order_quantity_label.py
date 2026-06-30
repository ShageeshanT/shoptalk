from shoptalk.order_quantity_label import order_quantity_label


def test_order_quantity_label():
    assert order_quantity_label(8) == "bulk"
