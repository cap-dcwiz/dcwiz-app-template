from fastapi import APIRouter
from dcwiz_app_utils.response import wrap_response

router = APIRouter()


@router.on_event("startup")
async def startup():
    from dcwiz_app_utils.app import config

    # TODO: initialize...


# Define your endpoints here

@router.get("/health")
@wrap_response()
async def health():
    return {"status": "ok"}
