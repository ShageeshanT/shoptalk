from shoptalk.price_display import price_display

def test_price_display():
    assert price_display(1200) == "LKR 1,200.00"
