from shoptalk.task_urgency_label import task_urgency_label

def test_task_urgency_label_thresholds():
    assert task_urgency_label(1) == 'Immediate task'
    assert task_urgency_label(6) == 'Today task'
    assert task_urgency_label(24) == 'Tomorrow task'

def test_task_urgency_label_invalid_value():
    assert task_urgency_label("bad") == 'Later task'
