from shoptalk.payment_followup_label import label_payment_followup


def test_payment_followup_label():
    assert label_payment_followup(24) == "send reminder"
