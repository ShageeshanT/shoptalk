from shoptalk.reply_quality_score import reply_quality_score

def test_reply_quality_score_stays_in_bounds():
    assert 0 <= reply_quality_score(0, 0, 0) <= 100
    assert 0 <= reply_quality_score(5, 5, 5) <= 100

def test_reply_quality_score_responds_to_stronger_signal():
    assert reply_quality_score(5, 5, 5) >= reply_quality_score(0, 0, 0)
