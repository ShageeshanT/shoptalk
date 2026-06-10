from shoptalk.followup_age_label import followup_age_label

def test_followup_age_label_thresholds():
    assert followup_age_label(0) == 'Due today'
    assert followup_age_label(2) == 'Recently due'
    assert followup_age_label(7) == 'Overdue'

def test_followup_age_label_invalid_value():
    assert followup_age_label("bad") == 'Very overdue'
