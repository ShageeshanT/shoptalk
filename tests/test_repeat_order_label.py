from shoptalk.repeat_order_label import repeat_order_label

def test_repeat_order_label_thresholds():
    assert repeat_order_label(10) == 'Loyal buyer'
    assert repeat_order_label(3) == 'Repeat buyer'
    assert repeat_order_label(1) == 'Second order'

def test_repeat_order_label_invalid_value():
    assert repeat_order_label("bad") == 'First order'
