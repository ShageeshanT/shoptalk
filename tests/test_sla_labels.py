from shoptalk.sla_labels import sla_label


def test_sla_label_fresh():
    assert sla_label(10) == "fresh"


def test_sla_label_waiting():
    assert sla_label(60) == "waiting"


def test_sla_label_overdue():
    assert sla_label(240) == "overdue"
