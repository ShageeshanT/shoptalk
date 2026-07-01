from shoptalk.cod_confirm_score import cod_confirm_score


def test_cod_confirm_score_bounds():
    assert 0 <= cod_confirm_score(40000, 3, False) <= 100


def test_cod_confirm_score_separates_strong_and_weak_signal():
    assert cod_confirm_score(40000, 3, False) > cod_confirm_score(1000, 72, True)
