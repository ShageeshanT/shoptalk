from shoptalk.order_margin_label import order_margin_label

def test_order_margin_label_thresholds():
    assert order_margin_label(50) == 'High margin'
    assert order_margin_label(25) == 'Good margin'
    assert order_margin_label(5) == 'Thin margin'

def test_order_margin_label_invalid_value():
    assert order_margin_label("bad") == 'No margin'
