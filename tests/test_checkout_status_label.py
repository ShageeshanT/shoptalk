from shoptalk.checkout_status_label import checkout_status_label

def test_checkout_status_label_known_values():
    assert checkout_status_label('ready') == 'Checkout ready'
    assert checkout_status_label('sent') == 'Checkout sent'
    assert checkout_status_label('paid') == 'Checkout paid'

def test_checkout_status_label_unknown_value():
    assert checkout_status_label("") == 'Checkout draft'
