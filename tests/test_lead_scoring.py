from shoptalk.lead_scoring import lead_label, lead_score


def test_lead_score_hot():
    assert lead_score("Can I order today?") >= 3
    assert lead_label("Can I order today?") == "hot"


def test_lead_label_warm_and_cold():
    assert lead_label("price please") == "warm"
    assert lead_label("hello") == "cold"
