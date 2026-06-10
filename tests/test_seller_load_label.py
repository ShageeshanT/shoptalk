from shoptalk.seller_load_label import seller_load_label

def test_seller_load_label_thresholds():
    assert seller_load_label(50) == 'Heavy load'
    assert seller_load_label(20) == 'Busy load'
    assert seller_load_label(5) == 'Light load'

def test_seller_load_label_invalid_value():
    assert seller_load_label("bad") == 'Clear load'
