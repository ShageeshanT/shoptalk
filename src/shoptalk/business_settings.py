from pydantic import BaseModel, Field


class BusinessSettings(BaseModel):
    auto_create_followups: bool = True
    require_human_approval: bool = True
    default_deposit_percent: int = Field(default=50, ge=0, le=100)
    quiet_hours_start: str = '21:00'
    quiet_hours_end: str = '08:00'


def default_settings() -> BusinessSettings:
    return BusinessSettings()
