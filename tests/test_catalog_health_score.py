from shoptalk.catalog_health_score import catalog_health_score

def test_catalog_health_score_stays_in_bounds():
    assert 0 <= catalog_health_score(0, 0, 0) <= 100
    assert 0 <= catalog_health_score(5, 5, 5) <= 100

def test_catalog_health_score_responds_to_stronger_signal():
    assert catalog_health_score(5, 5, 5) >= catalog_health_score(0, 0, 0)
