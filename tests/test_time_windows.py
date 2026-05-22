from shoptalk.time_windows import detect_time_window


def test_detect_time_window_finds_named_window() -> None:
    assert detect_time_window("Saturday evening please") == "evening"


def test_detect_time_window_finds_clock_time() -> None:
    assert detect_time_window("pickup at 6pm") == "6pm"
