from urllib.parse import urlsplit, urlunsplit


def mask_database_url(url: str | None) -> str | None:
    if not url:
        return url
    parsed = urlsplit(url)
    if not parsed.password:
        return url
    host = parsed.hostname or ""
    if parsed.port:
        host = f"{host}:{parsed.port}"
    username = parsed.username or ""
    netloc = f"{username}:***@{host}"
    return urlunsplit((parsed.scheme, netloc, parsed.path, parsed.query, parsed.fragment))
