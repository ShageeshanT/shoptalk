from shoptalk.customer_contact_quality import contact_quality_label, contact_quality_score


def test_contact_quality_scores_known_routes():
    assert contact_quality_score(phone="+9477", channel_id="wa_1") == 75


def test_contact_quality_labels_strength():
    assert contact_quality_label(90) == "strong"
    assert contact_quality_label(50) == "usable"
    assert contact_quality_label(10) == "weak"
