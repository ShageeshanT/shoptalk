from shoptalk.payment_method_label import payment_method_label

def test_payment_method_label_known_values():
    assert payment_method_label('card') == 'Card'
    assert payment_method_label('bank') == 'Bank transfer'
    assert payment_method_label('cash') == 'Cash'

def test_payment_method_label_unknown_value():
    assert payment_method_label("") == 'Other payment'
