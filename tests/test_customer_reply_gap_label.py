    from shoptalk.customer_reply_gap_label import classify_customer_reply_gap


    def test_classify_customer_reply_gap_labels_key_states():
        assert classify_customer_reply_gap(-1) == 'Recent'
assert classify_customer_reply_gap(3) == 'Follow up'
assert classify_customer_reply_gap(50) == 'Dormant'
