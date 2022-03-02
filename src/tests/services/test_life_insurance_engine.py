import pytest
from models.personal_data import MaritalStatusEnum
from services.life_insurance_engine import LifeInsuranceEngine
from services.risk_engine import ClassificationParams, InsuranceProfileEnum


class TestLifeInsuranceEngine:
    @pytest.mark.parametrize(
        "personal_data__age, personal_data__marital_status, personal_data__dependents, expected_profile",
        [
            (35, MaritalStatusEnum.SINGLE, 1, InsuranceProfileEnum.REGULAR),
            (20, MaritalStatusEnum.SINGLE, 0, InsuranceProfileEnum.ECONOMIC),
            (65, MaritalStatusEnum.SINGLE, 1, InsuranceProfileEnum.INELIGIBLE),
            (50, MaritalStatusEnum.MARRIED, 2, InsuranceProfileEnum.RESPONSIBLE),
        ],
    )
    def test_when_valid_data__should_calculate_profile_correctly(
        self, classification_params: ClassificationParams, expected_profile: str
    ):
        life_insurance_engine = LifeInsuranceEngine()
        profile = life_insurance_engine.determine_profile(
            classification_params=classification_params
        )

        assert profile == expected_profile
