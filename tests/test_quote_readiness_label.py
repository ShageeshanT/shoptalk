    from shoptalk.quote_readiness_label import classify_quote_readiness


    def test_classify_quote_readiness_labels_key_states():
        assert classify_quote_readiness(-1) == 'Ready'
assert classify_quote_readiness(1) == 'Review'
assert classify_quote_readiness(3) == 'Incomplete'
