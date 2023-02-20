from .schemas import HealthStatus
from fastapi import APIRouter
from dcwiz_app_utils.response import wrap_response

router = APIRouter()


@router.on_event("startup")
async def startup():
    from dcwiz_app_utils.app import config

    # TODO: initialize...


@router.get("/health")
@wrap_response()
async def health() -> HealthStatus:
    return {"status": "ok"}


# Define your endpoints here
