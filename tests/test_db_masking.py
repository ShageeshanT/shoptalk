from shoptalk.db_masking import mask_database_url


def test_mask_database_url_hides_password():
    masked = mask_database_url("postgresql://user:secret@example.com:5432/app")
    assert masked == "postgresql://user:***@example.com:5432/app"
    assert "secret" not in masked


def test_mask_database_url_leaves_sqlite_paths():
    assert mask_database_url("sqlite+pysqlite:///data/app.db") == "sqlite+pysqlite:///data/app.db"
