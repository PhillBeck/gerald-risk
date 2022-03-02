from pydantic import BaseModel, validator


class VehicleData(BaseModel):
    year: int

    @validator("year")
    def _validate_year(cls, year: int) -> int:
        if year < 1900:
            raise ValueError("Vehicle year cannot be less than 1900")

        return year
