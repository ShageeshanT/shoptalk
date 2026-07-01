from shoptalk.invoice_followup_score import invoice_followup_score

def test_invoice_followup_score_stays_in_bounds():
    assert 0 <= invoice_followup_score(0, 0, 0) <= 100
    assert 0 <= invoice_followup_score(5, 5, 5) <= 100

def test_invoice_followup_score_responds_to_stronger_signal():
    assert invoice_followup_score(5, 5, 5) >= invoice_followup_score(0, 0, 0)
