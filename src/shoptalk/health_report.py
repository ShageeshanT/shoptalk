from pydantic import BaseModel


class DependencyHealth(BaseModel):
    name: str
    ok: bool
    detail: str = 'ok'


class HealthReport(BaseModel):
    service: str = 'shoptalk'
    dependencies: list[DependencyHealth]

    @property
    def ok(self) -> bool:
        return all(item.ok for item in self.dependencies)
