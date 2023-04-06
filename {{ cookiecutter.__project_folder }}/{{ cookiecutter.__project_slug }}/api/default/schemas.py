from dcwiz_app_utils import ResponseSchema
from pydantic import Field, validator


class HealthStatus(ResponseSchema):
    status: str


# Define your Pydantic models
