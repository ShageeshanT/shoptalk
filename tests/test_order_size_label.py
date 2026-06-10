from shoptalk.order_size_label import order_size_label

def test_order_size_label_thresholds():
    assert order_size_label(50000) == 'Large order'
    assert order_size_label(15000) == 'Medium order'
    assert order_size_label(1000) == 'Small order'

def test_order_size_label_invalid_value():
    assert order_size_label("bad") == 'Tiny order'
