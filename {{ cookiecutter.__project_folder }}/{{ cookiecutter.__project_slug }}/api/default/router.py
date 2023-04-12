from dcwiz_app_utils import get_config, APIRouter

from .schemas import HealthStatus

router = APIRouter()
config = get_config()


@router.on_event("startup")
async def startup():
    pass

    # TODO: initialize...


@router.get("/health")
async def health() -> HealthStatus:
    return HealthStatus(status="OK")


# Define your endpoints here
