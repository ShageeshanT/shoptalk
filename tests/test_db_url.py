from shoptalk.db_url import build_sqlite_url, default_database_path


def test_build_sqlite_url_for_memory_database():
    assert build_sqlite_url(":memory:") == "sqlite+pysqlite:///:memory:"


def test_default_database_path_points_to_data_folder():
    assert str(default_database_path()).endswith("data/shoptalk.sqlite3")
