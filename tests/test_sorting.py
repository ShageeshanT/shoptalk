from datetime import datetime, timezone
from types import SimpleNamespace

from shoptalk.sorting import newest_first


def test_newest_first_sorts_by_timestamp_field() -> None:
    older = SimpleNamespace(created_at=datetime(2026, 1, 1, tzinfo=timezone.utc))
    newer = SimpleNamespace(created_at=datetime(2026, 1, 2, tzinfo=timezone.utc))
    assert newest_first([older, newer]) == [newer, older]
