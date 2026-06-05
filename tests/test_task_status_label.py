from shoptalk.task_status_label import task_status_label

def test_task_status_label():
    assert task_status_label(False)=="Open"