from shoptalk.order_value_band import order_value_band


def test_order_value_band():
    assert order_value_band(12000) == "high"
