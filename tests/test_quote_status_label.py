from shoptalk.quote_status_label import quote_status_label

def test_quote_status_label_known_values():
    assert quote_status_label('accepted') == 'Quote accepted'
    assert quote_status_label('sent') == 'Quote sent'
    assert quote_status_label('expired') == 'Quote expired'

def test_quote_status_label_unknown_value():
    assert quote_status_label("") == 'Quote draft'
