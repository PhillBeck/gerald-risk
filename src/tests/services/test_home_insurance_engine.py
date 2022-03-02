import pytest
from models.house_data import HouseOwnershipStatusEnum
from models.personal_data import MaritalStatusEnum
from services.home_insurance_engine import HomeInsuranceEngine
from services.risk_engine import ClassificationParams, InsuranceProfileEnum


class TestHomeInsuranceEngine:
    @pytest.mark.parametrize(
        "personal_data__age, personal_data__income, house_data__ownership_status, expected_profile",
        [
            (
                20,
                250_000,
                HouseOwnershipStatusEnum.OWNED,
                InsuranceProfileEnum.ECONOMIC,
            ),
            (
                50,
                50_000,
                HouseOwnershipStatusEnum.MORTGAGED,
                InsuranceProfileEnum.REGULAR,
            ),
        ],
    )
    def test_when_valid_data__should_calculate_profile_correctly(
        self, classification_params: ClassificationParams, expected_profile: str
    ):
        life_insurance_engine = HomeInsuranceEngine()
        profile = life_insurance_engine.determine_profile(
            classification_params=classification_params
        )

        assert profile == expected_profile
