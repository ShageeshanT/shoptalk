from shoptalk.fulfillment_mode_label import fulfillment_mode_label

def test_fulfillment_mode_label_known_values():
    assert fulfillment_mode_label('delivery') == 'Delivery'
    assert fulfillment_mode_label('pickup') == 'Pickup'
    assert fulfillment_mode_label('digital') == 'Digital'

def test_fulfillment_mode_label_unknown_value():
    assert fulfillment_mode_label("") == 'Manual fulfillment'
