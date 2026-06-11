from shoptalk.catalog_cleanup_label import classify_catalog_cleanup


def test_classify_catalog_cleanup_labels_key_states():
    assert classify_catalog_cleanup(-1) == 'Clean'
    assert classify_catalog_cleanup(1) == 'Review'
    assert classify_catalog_cleanup(30) == 'Messy'
