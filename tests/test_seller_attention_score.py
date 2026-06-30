from shoptalk.seller_attention_score import seller_attention_score

def test_seller_attention_score_weights_overdue():
    assert seller_attention_score(2, 3) == 11
