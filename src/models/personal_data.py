from enum import Enum, IntEnum
from typing import List

from pydantic import BaseModel, validator


class MaritalStatusEnum(str, Enum):
    SINGLE = "single"
    MARRIED = "married"


class PersonalData(BaseModel):
    age: int
    dependents: int
    income: int
    marital_status: MaritalStatusEnum
    risk_questions: List[int]

    @validator("age")
    def _validate_age(cls, age: int) -> int:
        if age < 0:
            raise ValueError("age should be larger than 0")

        return age

    @validator("dependents")
    def _validate_dependents(cls, dependents: int) -> int:
        if dependents < 0:
            raise ValueError("dependents should be larger than 0")

        return dependents

    @validator("risk_questions")
    def _validate_risk_questions(cls, risk_questions: List[int]) -> List[int]:
        if len(risk_questions) != 3:
            raise ValueError("risk_questions should have exactly 3 answers")

        return risk_questions
