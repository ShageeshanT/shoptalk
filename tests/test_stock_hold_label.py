    from shoptalk.stock_hold_label import classify_stock_hold


    def test_classify_stock_hold_labels_key_states():
        assert classify_stock_hold(-1) == 'Fresh'
assert classify_stock_hold(3) == 'Held'
assert classify_stock_hold(30) == 'Release'
