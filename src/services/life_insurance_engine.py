from models.personal_data import MaritalStatusEnum
from services.risk_engine import (
    ClassificationParams,
    InsuranceProfileEnum,
    calculate_base_risk,
    define_profile,
)


class LifeInsuranceEngine:
    def _validate_params(self, classification_params: ClassificationParams):
        if not classification_params.personal_data:
            raise ValueError(
                "Cannot determine life insurance profile without personal data"
            )

    def determine_profile(
        self, classification_params: ClassificationParams
    ) -> InsuranceProfileEnum:
        self._validate_params(classification_params)

        if classification_params.personal_data.age > 60:
            return InsuranceProfileEnum.INELIGIBLE

        risk = calculate_base_risk(classification_params)

        if classification_params.personal_data.dependents > 0:
            risk += 1

        if (
            classification_params.personal_data.marital_status
            == MaritalStatusEnum.MARRIED
        ):
            risk += 1

        return define_profile(risk)
