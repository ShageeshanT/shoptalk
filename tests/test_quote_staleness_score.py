from shoptalk.quote_staleness_score import quote_staleness_score


def test_quote_staleness_score_bounds():
    assert 0 <= quote_staleness_score(80, True, False) <= 100


def test_quote_staleness_score_separates_strong_and_weak_signal():
    assert quote_staleness_score(80, True, False) > quote_staleness_score(2, False, True)
