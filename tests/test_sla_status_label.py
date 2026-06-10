from shoptalk.sla_status_label import sla_status_label

def test_sla_status_label_thresholds():
    assert sla_status_label(5) == 'Fast response'
    assert sla_status_label(30) == 'Within SLA'
    assert sla_status_label(120) == 'Slow response'

def test_sla_status_label_invalid_value():
    assert sla_status_label("bad") == 'Critical delay'
