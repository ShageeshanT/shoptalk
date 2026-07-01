from shoptalk.cash_collection_score import cash_collection_score


def test_cash_collection_score_bounds():
    assert 0 <= cash_collection_score(0, 0) <= 100


def test_cash_collection_score_rises_with_old_large_unpaid_invoice():
    assert cash_collection_score(60000, 20, 3) > cash_collection_score(1000, 1, 0)
