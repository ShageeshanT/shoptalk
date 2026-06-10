from shoptalk.discount_status_label import discount_status_label

def test_discount_status_label_thresholds():
    assert discount_status_label(30) == 'Heavy discount'
    assert discount_status_label(10) == 'Standard discount'
    assert discount_status_label(1) == 'Small discount'

def test_discount_status_label_invalid_value():
    assert discount_status_label("bad") == 'No discount'
