from pathlib import Path


def test_env_example_documents_database_url():
    assert "DATABASE_URL=" in Path(".env.example").read_text()
