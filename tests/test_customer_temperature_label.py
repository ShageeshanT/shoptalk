    from shoptalk.customer_temperature_label import classify_customer_temperature


    def test_classify_customer_temperature_labels_key_states():
        assert classify_customer_temperature(-1) == 'Cold'
assert classify_customer_temperature(40) == 'Warm'
assert classify_customer_temperature(80) == 'Hot'
