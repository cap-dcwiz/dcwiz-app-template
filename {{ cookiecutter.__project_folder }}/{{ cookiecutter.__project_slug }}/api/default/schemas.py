from dcwiz_app_utils import ResponseSchema
from pydantic import Field, validator


class HealthStatus(ResponseResultSchema):
    status: str


# Define your Pydantic models
