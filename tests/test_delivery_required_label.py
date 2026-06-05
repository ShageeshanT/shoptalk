from shoptalk.delivery_required_label import delivery_required_label

def test_delivery_required_label():
    assert delivery_required_label(True)=="Delivery needed"