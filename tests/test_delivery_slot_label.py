    from shoptalk.delivery_slot_label import classify_delivery_slot


    def test_classify_delivery_slot_labels_key_states():
        assert classify_delivery_slot(-1) == 'Full'
assert classify_delivery_slot(1) == 'Limited'
assert classify_delivery_slot(3) == 'Available'
