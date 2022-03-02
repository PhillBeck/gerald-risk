from pydantic import BaseModel
from enum import Enum


class HouseOwnershipStatusEnum(str, Enum):
    OWNED = "owned"
    MORTGAGED = "mortgaged"


class HouseData(BaseModel):
    ownership_status: HouseOwnershipStatusEnum
