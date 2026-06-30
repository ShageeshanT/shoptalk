from shoptalk.catalog_photo_label import classify_catalog_photo


def test_classify_catalog_photo_labels_key_states():
    assert classify_catalog_photo(0) == "Photos ready"
    assert classify_catalog_photo(1) == "Add photos"
    assert classify_catalog_photo(5) == "Photo gap"
