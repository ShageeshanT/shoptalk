from shoptalk.buyer_intent_score import buyer_intent_score

def test_buyer_intent_score_stays_in_bounds():
    assert 0 <= buyer_intent_score(0, 0, 0) <= 100
    assert 0 <= buyer_intent_score(5, 5, 5) <= 100

def test_buyer_intent_score_responds_to_stronger_signal():
    assert buyer_intent_score(5, 5, 5) >= buyer_intent_score(0, 0, 0)
