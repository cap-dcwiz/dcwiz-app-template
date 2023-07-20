from dcwiz_app_utils import get_config, APIRouter
from fastapi import Depends
from fastapi.security import HTTPBearer

from .schemas import HealthStatus


router = APIRouter()
config = get_config()
auth_scheme = HTTPBearer()


@router.on_event("startup")
async def startup():
    pass

    # TODO: initialize...


@router.get("/health")
async def health() -> HealthStatus:
    return HealthStatus(status="OK")


@router.get("/")
async def first_endpoint(bearer=Depends(auth_scheme)):
    bearer = bearer.credentials
    raise NotImplementedError


# Define your endpoints here
