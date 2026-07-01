from shoptalk.supplier_reliability_score import supplier_reliability_score

def test_supplier_reliability_score_stays_in_bounds():
    assert 0 <= supplier_reliability_score(0, 0, 0) <= 100
    assert 0 <= supplier_reliability_score(5, 5, 5) <= 100

def test_supplier_reliability_score_responds_to_stronger_signal():
    assert supplier_reliability_score(5, 5, 5) >= supplier_reliability_score(0, 0, 0)
