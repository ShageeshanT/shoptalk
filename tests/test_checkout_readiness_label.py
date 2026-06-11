    from shoptalk.checkout_readiness_label import classify_checkout_readiness


    def test_classify_checkout_readiness_labels_key_states():
        assert classify_checkout_readiness(-1) == 'Blocked'
assert classify_checkout_readiness(2) == 'Almost ready'
assert classify_checkout_readiness(5) == 'Ready'
