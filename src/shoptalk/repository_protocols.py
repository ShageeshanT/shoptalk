from typing import Protocol, TypeVar

CreatePayload = TypeVar("CreatePayload")
Model = TypeVar("Model")


class CreateRepository(Protocol[CreatePayload, Model]):
    def create(self, payload: CreatePayload) -> Model: ...


class GetRepository(Protocol[Model]):
    def get(self, record_id) -> Model | None: ...


class BusinessScopedRepository(Protocol[Model]):
    def list_for_business(self, business_id) -> list[Model]: ...
