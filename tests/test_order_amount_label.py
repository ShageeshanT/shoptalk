from shoptalk.order_amount_label import order_amount_label

def test_order_amount_label():
    assert order_amount_label(1250) == "Rs 1,250.00"
    assert order_amount_label(None) == "Amount not set"