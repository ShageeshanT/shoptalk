from shoptalk.message_cleanup_score import message_cleanup_score


def test_message_cleanup_score_bounds():
    assert 0 <= message_cleanup_score(4, 3, False) <= 100


def test_message_cleanup_score_separates_strong_and_weak_signal():
    assert message_cleanup_score(4, 3, False) > message_cleanup_score(0, 0, True)
