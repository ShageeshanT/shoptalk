    from shoptalk.stock_action_label import classify_stock_action


    def test_classify_stock_action_labels_key_states():
        assert classify_stock_action(-1) == 'Restock'
assert classify_stock_action(1) == 'Watch'
assert classify_stock_action(6) == 'Healthy'
