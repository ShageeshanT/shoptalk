from shoptalk.approval_queue_score import approval_queue_score


def test_approval_queue_score_bounds():
    assert 0 <= approval_queue_score(8, 200, 2) <= 100


def test_approval_queue_score_separates_strong_and_weak_signal():
    assert approval_queue_score(8, 200, 2) > approval_queue_score(0, 0, 0)
