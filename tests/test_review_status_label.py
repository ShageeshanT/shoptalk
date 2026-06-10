from shoptalk.review_status_label import review_status_label

def test_review_status_label_thresholds():
    assert review_status_label(5) == 'Excellent review'
    assert review_status_label(4) == 'Good review'
    assert review_status_label(3) == 'Mixed review'

def test_review_status_label_invalid_value():
    assert review_status_label("bad") == 'Needs attention'
