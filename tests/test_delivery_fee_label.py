from shoptalk.delivery_fee_label import delivery_fee_label

def test_delivery_fee_label():
    assert delivery_fee_label(0)=="Free delivery"