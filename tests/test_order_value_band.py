from shoptalk.order_value_band import order_value_band

def test_order_value_band():
    assert order_value_band(1200) == "starter"
    assert order_value_band(5000) == "standard"
    assert order_value_band(15000) == "premium"
