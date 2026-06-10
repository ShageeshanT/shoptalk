from shoptalk.customer_segment_label import customer_segment_label

def test_customer_segment_label_known_values():
    assert customer_segment_label('vip') == 'VIP'
    assert customer_segment_label('repeat') == 'Repeat customer'
    assert customer_segment_label('new') == 'New customer'

def test_customer_segment_label_unknown_value():
    assert customer_segment_label("") == 'Unsegmented'
