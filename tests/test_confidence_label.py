from shoptalk.confidence_label import confidence_label

def test_confidence_label():
    assert confidence_label(.81)=="High confidence"