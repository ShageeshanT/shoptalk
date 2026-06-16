"""Application configuration loaded from environment variables."""

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All runtime settings for ShopTalk.

    Values are read from environment variables or a .env file.
    See .env.example for the full list of supported keys.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # AI
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    # Database
    database_url: str = "sqlite:///./shoptalk.db"

    # Security
    secret_key: str = "dev-secret-change-in-production"
    seller_api_key: str = ""

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    environment: str = "development"

    # WhatsApp
    whatsapp_verify_token: str = ""
    whatsapp_access_token: str = ""
    whatsapp_phone_number_id: str = ""

    # Telegram
    telegram_bot_token: str = ""

    # Logging
    log_level: str = "INFO"

    # Rate limiting
    rate_limit_per_minute: int = 60

    @property
    def is_production(self) -> bool:
        """Return True when running in production mode."""
        return self.environment.lower() == "production"

    @property
    def debug(self) -> bool:
        """Return True when debug mode is active."""
        return not self.is_production


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance.

    Use this as a FastAPI dependency::

        from shoptalk.config import get_settings

        @router.get("/example")
        def example(settings: Settings = Depends(get_settings)):
            ...
    """
    return Settings()
