    from shoptalk.promo_window_label import classify_promo_window


    def test_classify_promo_window_labels_key_states():
        assert classify_promo_window(-1) == 'Expired'
assert classify_promo_window(0) == 'Last call'
assert classify_promo_window(3) == 'Active'
