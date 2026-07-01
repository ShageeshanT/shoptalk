from shoptalk.support_priority_score import support_priority_score

def test_support_priority_score_stays_in_bounds():
    assert 0 <= support_priority_score(0, 0, 0) <= 100
    assert 0 <= support_priority_score(5, 5, 5) <= 100

def test_support_priority_score_responds_to_stronger_signal():
    assert support_priority_score(5, 5, 5) >= support_priority_score(0, 0, 0)
