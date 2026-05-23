from shoptalk.config import Settings


def test_settings_accept_database_url():
    settings = Settings(database_url="sqlite+pysqlite:///:memory:")
    assert settings.database_url.endswith(":memory:")
