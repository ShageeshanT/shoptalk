from shoptalk.fulfillment_confidence_score import fulfillment_confidence_score

def test_fulfillment_confidence_score_stays_in_bounds():
    assert 0 <= fulfillment_confidence_score(0, 0, 0) <= 100
    assert 0 <= fulfillment_confidence_score(5, 5, 5) <= 100

def test_fulfillment_confidence_score_responds_to_stronger_signal():
    assert fulfillment_confidence_score(5, 5, 5) >= fulfillment_confidence_score(0, 0, 0)
