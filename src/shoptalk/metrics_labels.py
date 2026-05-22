def metric_name(*parts: str) -> str:
    return '.'.join(part.strip().lower().replace(' ', '_') for part in parts if part.strip())
