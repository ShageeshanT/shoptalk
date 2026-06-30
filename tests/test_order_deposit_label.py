from shoptalk.order_deposit_label import order_deposit_label

def test_order_deposit_label():
    assert order_deposit_label(1000, 1000) == "paid"
    assert order_deposit_label(1000, 200) == "deposit needed"
