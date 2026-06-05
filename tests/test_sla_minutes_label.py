from shoptalk.sla_minutes_label import sla_minutes_label

def test_sla_minutes_label():
    assert sla_minutes_label(75)=="1h 15m"