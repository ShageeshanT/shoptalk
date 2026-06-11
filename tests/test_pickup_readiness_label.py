    from shoptalk.pickup_readiness_label import classify_pickup_readiness


    def test_classify_pickup_readiness_labels_key_states():
        assert classify_pickup_readiness(-1) == 'Late'
assert classify_pickup_readiness(0) == 'Soon'
assert classify_pickup_readiness(5) == 'Scheduled'
