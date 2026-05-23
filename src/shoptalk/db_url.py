from pathlib import Path


def build_sqlite_url(path: str | Path) -> str:
    db_path = Path(path).expanduser()
    if str(db_path) == ":memory:":
        return "sqlite+pysqlite:///:memory:"
    return f"sqlite+pysqlite:///{db_path}"


def default_database_path() -> Path:
    return Path("data") / "shoptalk.sqlite3"
