    from shoptalk.seller_next_action_label import classify_seller_next_action


    def test_classify_seller_next_action_labels_key_states():
        assert classify_seller_next_action(-1) == 'Later'
assert classify_seller_next_action(3) == 'Today'
assert classify_seller_next_action(10) == 'Now'
