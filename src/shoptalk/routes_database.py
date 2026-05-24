from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from shoptalk.db_health import database_health
from shoptalk.db_readiness import database_readiness
from shoptalk.db_runtime import get_db_session, get_engine

router = APIRouter(prefix="/database", tags=["database"])


@router.get("/health")
def database_health_endpoint(session: Session = Depends(get_db_session)):
    return database_health(session)


@router.get("/readiness")
def database_readiness_endpoint():
    return database_readiness(get_engine())
