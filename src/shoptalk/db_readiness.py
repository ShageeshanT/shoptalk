from sqlalchemy import inspect

REQUIRED_TABLES = {"businesses", "customers", "orders", "messages", "follow_ups"}


def database_readiness(engine) -> dict[str, object]:
    existing = set(inspect(engine).get_table_names())
    missing = sorted(REQUIRED_TABLES - existing)
    return {"ready": not missing, "missing_tables": missing, "required_tables": sorted(REQUIRED_TABLES)}
