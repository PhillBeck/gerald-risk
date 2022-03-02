from pydantic import BaseModel
from enum import Enum


class InsuranceLineEnum(str, Enum):
    ECONOMIC = "economic"
    REGULAR = "regular"
    RESPONSIBLE = "responsible"


class ResponseModel(BaseModel):
    auto: str
    disability: str
    home: str
    life: str
