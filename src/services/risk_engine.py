from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional, Protocol

from models import PersonalData, HouseData, VehicleData


@dataclass
class ClassificationParams:
    personal_data: Optional[PersonalData]
    house_data: Optional[HouseData]
    vehicle_data: Optional[VehicleData]


class InsuranceProfileEnum(str, Enum):
    ECONOMIC = "economic"
    REGULAR = "regular"
    RESPONSIBLE = "responsible"
    INELIGIBLE = "ineligible"


class Engine(Protocol):
    def determine_profile(
        self, classification_params: ClassificationParams
    ) -> InsuranceProfileEnum:
        ...


def calculate_base_risk(classification_params: ClassificationParams) -> int:
    if not classification_params.personal_data:
        raise ValueError("")
    base_risk = sum(classification_params.personal_data.risk_questions)

    if classification_params.personal_data.age < 30:
        base_risk -= 2
    if 30 < classification_params.personal_data.age < 40:
        base_risk -= 1

    if classification_params.personal_data.income > 200_000:
        base_risk -= 1

    return base_risk


def define_profile(risk: int) -> InsuranceProfileEnum:
    if risk <= 0:
        return InsuranceProfileEnum.ECONOMIC

    if risk >= 3:
        return InsuranceProfileEnum.RESPONSIBLE

    return InsuranceProfileEnum.REGULAR


@dataclass
class RiskService:
    registered_engines: Dict[str, Engine] = field(default_factory=dict)

    def register_engine(self, name: str, engine: Engine):
        self.registered_engines[name] = engine

    def determine_profiles(
        self, classification_params: ClassificationParams
    ) -> Dict[str, InsuranceProfileEnum]:
        return {
            name: engine.determine_profile(classification_params=classification_params)
            for name, engine in self.registered_engines.items()
        }
