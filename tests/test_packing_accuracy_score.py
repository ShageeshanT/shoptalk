from shoptalk.packing_accuracy_score import packing_accuracy_score

def test_packing_accuracy_score_stays_in_bounds():
    assert 0 <= packing_accuracy_score(0, 0, 0) <= 100
    assert 0 <= packing_accuracy_score(5, 5, 5) <= 100

def test_packing_accuracy_score_responds_to_stronger_signal():
    assert packing_accuracy_score(5, 5, 5) >= packing_accuracy_score(0, 0, 0)
