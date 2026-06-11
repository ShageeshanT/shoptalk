    from shoptalk.delivery_fee_tier import classify_delivery_fee_tier


    def test_classify_delivery_fee_tier_labels_key_states():
        assert classify_delivery_fee_tier(-1) == 'Free'
assert classify_delivery_fee_tier(1) == 'Standard'
