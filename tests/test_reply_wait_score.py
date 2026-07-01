from shoptalk.reply_wait_score import reply_wait_score


def test_reply_wait_score_bounds():
    assert 0 <= reply_wait_score(240, 5, 0) <= 100


def test_reply_wait_score_separates_strong_and_weak_signal():
    assert reply_wait_score(240, 5, 0) > reply_wait_score(5, 0, 2)
