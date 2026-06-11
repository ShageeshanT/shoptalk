    from shoptalk.customer_value_tier import classify_customer_value_tier


    def test_classify_customer_value_tier_labels_key_states():
        assert classify_customer_value_tier(-1) == 'Starter'
assert classify_customer_value_tier(0) == 'Starter'
