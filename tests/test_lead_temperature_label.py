from shoptalk.lead_temperature_label import label_lead_temperature


def test_lead_temperature_label():
    assert label_lead_temperature(82) == "hot"
