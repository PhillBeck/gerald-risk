from models.house_data import HouseOwnershipStatusEnum
from models.personal_data import MaritalStatusEnum
from services.risk_engine import (
    ClassificationParams,
    InsuranceProfileEnum,
    calculate_base_risk,
    define_profile,
)


class DisabilityInsuranceEngine:
    def _validate_params(self, classification_params: ClassificationParams):
        if not classification_params.personal_data:
            raise ValueError(
                "Cannot determine disability insurance profile without personal data"
            )

    def determine_profile(
        self, classification_params: ClassificationParams
    ) -> InsuranceProfileEnum:
        self._validate_params(classification_params)

        if not classification_params.personal_data.income:
            return InsuranceProfileEnum.INELIGIBLE

        if classification_params.personal_data.age > 60:
            return InsuranceProfileEnum.INELIGIBLE

        risk = calculate_base_risk(classification_params)

        if (
            classification_params.house_data
            and classification_params.house_data.ownership_status
            == HouseOwnershipStatusEnum.MORTGAGED
        ):
            risk += 1

        if classification_params.personal_data.dependents > 0:
            risk += 1

        if (
            classification_params.personal_data.marital_status
            == MaritalStatusEnum.MARRIED
        ):
            risk -= 1

        return define_profile(risk)
