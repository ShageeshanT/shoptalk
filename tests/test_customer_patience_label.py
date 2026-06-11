    from shoptalk.customer_patience_label import classify_customer_patience


    def test_classify_customer_patience_labels_key_states():
        assert classify_customer_patience(-1) == 'Fresh'
assert classify_customer_patience(30) == 'Waiting'
assert classify_customer_patience(100) == 'At risk'
