from shoptalk.catalog_match_score import catalog_match_score

def test_catalog_match_score():
    assert catalog_match_score("chocolate cake", "dark chocolate cake") == 2
