from typing import Optional
from models.house_data import HouseData
from models.personal_data import PersonalData
from models.vehicle_data import VehicleData
from pydantic import BaseModel


class RequestModel(PersonalData):
    house: Optional[HouseData]
    vehicle: Optional[VehicleData]
