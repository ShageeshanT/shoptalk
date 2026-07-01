from shoptalk.catalog_freshness_score import catalog_freshness_score


def test_catalog_freshness_score_bounds():
    assert 0 <= catalog_freshness_score(45, 5, 4) <= 100


def test_catalog_freshness_score_separates_strong_and_weak_signal():
    assert catalog_freshness_score(45, 5, 4) > catalog_freshness_score(1, 0, 0)
