from shoptalk.seller_capacity_label import classify_seller_capacity


def test_classify_seller_capacity_labels_key_states():
    assert classify_seller_capacity(-1) == 'Full'
    assert classify_seller_capacity(1) == 'Limited'
    assert classify_seller_capacity(4) == 'Open'
