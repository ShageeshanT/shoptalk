from shoptalk.quote_expiry_label import classify_quote_expiry


def test_classify_quote_expiry_labels_key_states():
    assert classify_quote_expiry(-1) == 'Expired'
    assert classify_quote_expiry(1) == 'Soon'
    assert classify_quote_expiry(30) == 'Valid'
