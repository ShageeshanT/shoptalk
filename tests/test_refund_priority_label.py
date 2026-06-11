    from shoptalk.refund_priority_label import classify_refund_priority


    def test_classify_refund_priority_labels_key_states():
        assert classify_refund_priority(-1) == 'New'
assert classify_refund_priority(2) == 'Review'
assert classify_refund_priority(6) == 'Escalate'
