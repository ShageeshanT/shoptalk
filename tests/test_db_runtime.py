from shoptalk import db_runtime


def test_get_session_factory_is_cached(monkeypatch):
    db_runtime.get_engine.cache_clear()
    db_runtime.get_session_factory.cache_clear()
    monkeypatch.setattr("shoptalk.config.Settings.database_url", "sqlite+pysqlite:///:memory:", raising=False)
    first = db_runtime.get_session_factory()
    second = db_runtime.get_session_factory()
    assert first is second
    db_runtime.get_engine.cache_clear()
    db_runtime.get_session_factory.cache_clear()
