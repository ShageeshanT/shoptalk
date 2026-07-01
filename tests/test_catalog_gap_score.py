from shoptalk.catalog_gap_score import catalog_gap_score


def test_catalog_gap_score_bounds():
    assert 0 <= catalog_gap_score(5, 4, 8) <= 100


def test_catalog_gap_score_separates_strong_and_weak_signal():
    assert catalog_gap_score(5, 4, 8) > catalog_gap_score(0, 0, 0)
