from datetime import date
from services.risk_engine import (
    ClassificationParams,
    InsuranceProfileEnum,
    calculate_base_risk,
    define_profile,
)


class VehicleInsuranceEngine:
    def _validate_params(self, classification_params: ClassificationParams):
        if not classification_params.personal_data:
            raise ValueError(
                "Cannot determine vehicle insurance profile without personal data"
            )

    def determine_profile(
        self, classification_params: ClassificationParams
    ) -> InsuranceProfileEnum:
        self._validate_params(classification_params)

        if not classification_params.vehicle_data:
            return InsuranceProfileEnum.INELIGIBLE

        risk = calculate_base_risk(classification_params)

        if date.today().year - classification_params.vehicle_data.year < 5:
            risk += 1

        return define_profile(risk)
