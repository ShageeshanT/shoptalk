from shoptalk.refund_attention_score import refund_attention_score


def test_refund_attention_score_bounds():
    assert 0 <= refund_attention_score(25000, 8, True) <= 100


def test_refund_attention_score_separates_strong_and_weak_signal():
    assert refund_attention_score(25000, 8, True) > refund_attention_score(1000, 0, False)
