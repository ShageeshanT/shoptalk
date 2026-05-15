from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "ShopTalk"
    app_env: str = "development"
    database_url: str = "sqlite:///./shoptalk.db"
    ai_provider: str = "mock"
    ai_api_key: str | None = Field(default=None, repr=False)
    default_timezone: str = "Asia/Colombo"


@lru_cache
def get_settings() -> Settings:
    return Settings()
