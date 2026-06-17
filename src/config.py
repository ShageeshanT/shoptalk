"""Configuration management for ShopTalk."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Config:
    whatsapp_token: str = ""
    whatsapp_phone_id: str = ""
    webhook_verify_token: str = ""
    db_url: str = "sqlite:///shoptalk.db"
    redis_url: Optional[str] = None
    secret_key: str = "change-me-in-production"
    debug: bool = False
    port: int = 8000
    host: str = "0.0.0.0"
    business_name: str = "My Shop"
    default_currency: str = "USD"
    timezone: str = "UTC"
    rate_limit_requests: int = 60
    rate_limit_window: int = 60


def load_config() -> Config:
    return Config(
        whatsapp_token=os.environ.get("WHATSAPP_TOKEN", ""),
        whatsapp_phone_id=os.environ.get("WHATSAPP_PHONE_ID", ""),
        webhook_verify_token=os.environ.get("WEBHOOK_VERIFY_TOKEN", "shoptalk-verify"),
        db_url=os.environ.get("DATABASE_URL", "sqlite:///shoptalk.db"),
        redis_url=os.environ.get("REDIS_URL"),
        secret_key=os.environ.get("SECRET_KEY", "change-me-in-production"),
        debug=os.environ.get("DEBUG", "false").lower() == "true",
        port=int(os.environ.get("PORT", "8000")),
        host=os.environ.get("HOST", "0.0.0.0"),
        business_name=os.environ.get("BUSINESS_NAME", "My Shop"),
        default_currency=os.environ.get("DEFAULT_CURRENCY", "USD"),
        timezone=os.environ.get("TIMEZONE", "UTC"),
        rate_limit_requests=int(os.environ.get("RATE_LIMIT_REQUESTS", "60")),
        rate_limit_window=int(os.environ.get("RATE_LIMIT_WINDOW", "60")),
    )


def validate_config(config: Config) -> None:
    errors = []
    if not config.whatsapp_token:
        errors.append("WHATSAPP_TOKEN is required")
    if not config.whatsapp_phone_id:
        errors.append("WHATSAPP_PHONE_ID is required")
    if config.secret_key == "change-me-in-production" and not config.debug:
        errors.append("SECRET_KEY must be changed in production")
    if errors:
        raise ValueError("Configuration errors:\n" + "\n".join(f"  - {e}" for e in errors))


_config: Optional[Config] = None


def get_config() -> Config:
    global _config
    if _config is None:
        _config = load_config()
    return _config
