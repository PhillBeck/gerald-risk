from models.house_data import HouseOwnershipStatusEnum
from services.risk_engine import (
    ClassificationParams,
    InsuranceProfileEnum,
    calculate_base_risk,
    define_profile,
)


class HomeInsuranceEngine:
    def _validate_params(self, classification_params: ClassificationParams):
        if not classification_params.personal_data:
            raise ValueError(
                "Cannot determine home insurance profile without personal data"
            )

    def determine_profile(
        self, classification_params: ClassificationParams
    ) -> InsuranceProfileEnum:
        self._validate_params(classification_params)

        if not classification_params.house_data:
            return InsuranceProfileEnum.INELIGIBLE

        risk = calculate_base_risk(classification_params)

        if (
            classification_params.house_data.ownership_status
            == HouseOwnershipStatusEnum.MORTGAGED
        ):
            risk += 1

        return define_profile(risk)
