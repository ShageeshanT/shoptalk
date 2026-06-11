    from shoptalk.discount_depth_label import classify_discount_depth


    def test_classify_discount_depth_labels_key_states():
        assert classify_discount_depth(-1) == 'None'
assert classify_discount_depth(1) == 'Light'
assert classify_discount_depth(30) == 'Deep'
