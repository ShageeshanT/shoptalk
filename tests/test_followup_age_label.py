from shoptalk.followup_age_label import followup_age_label

def test_followup_age_label():
    assert followup_age_label(60) == "stale"
    assert followup_age_label(3) == "fresh"
