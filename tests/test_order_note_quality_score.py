from shoptalk.order_note_quality_score import order_note_quality_score


def test_order_note_quality_score_bounds():
    assert 0 <= order_note_quality_score(True, True, True, True, True) <= 100


def test_order_note_quality_score_separates_strong_and_weak_signal():
    assert order_note_quality_score(True, True, True, True, True) > order_note_quality_score(True, False, False, False, False)
