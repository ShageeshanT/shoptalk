    from shoptalk.checkout_friction_label import classify_checkout_friction


    def test_classify_checkout_friction_labels_key_states():
        assert classify_checkout_friction(-1) == 'Smooth'
assert classify_checkout_friction(1) == 'Needs info'
assert classify_checkout_friction(3) == 'Blocked'
