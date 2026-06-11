    from shoptalk.cart_recovery_label import classify_cart_recovery


    def test_classify_cart_recovery_labels_key_states():
        assert classify_cart_recovery(-1) == 'Active'
assert classify_cart_recovery(2) == 'Recover'
assert classify_cart_recovery(30) == 'Lost'
