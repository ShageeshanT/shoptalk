    from shoptalk.payment_followup_label import classify_payment_followup


    def test_classify_payment_followup_labels_key_states():
        assert classify_payment_followup(-1) == 'Fresh'
assert classify_payment_followup(2) == 'Nudge'
assert classify_payment_followup(5) == 'Escalate'
