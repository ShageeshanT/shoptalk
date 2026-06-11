    from shoptalk.customer_momentum_label import classify_customer_momentum


    def test_classify_customer_momentum_labels_key_states():
        assert classify_customer_momentum(-1) == 'New'
assert classify_customer_momentum(2) == 'Engaged'
assert classify_customer_momentum(5) == 'Loyal'
