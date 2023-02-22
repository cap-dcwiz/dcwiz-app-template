from dcwiz_app_utils import ORMLinkedSchema
from pydantic import BaseModel, Field, validator


class HealthStatus(BaseModel):
    status: str


# Define your Pydantic models
