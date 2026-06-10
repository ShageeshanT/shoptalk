from shoptalk.catalog_depth_label import catalog_depth_label

def test_catalog_depth_label_thresholds():
    assert catalog_depth_label(100) == 'Deep catalog'
    assert catalog_depth_label(25) == 'Healthy catalog'
    assert catalog_depth_label(1) == 'Starter catalog'

def test_catalog_depth_label_invalid_value():
    assert catalog_depth_label("bad") == 'No catalog'
