from fastapi import APIRouter

router = APIRouter()


@router.on_event("startup")
async def startup():
    from dcwiz_app_utils.app import config

    # TODO: initialize...


# Define your endpoints here
