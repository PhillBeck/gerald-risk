import pytest
from models.house_data import HouseOwnershipStatusEnum
from models.personal_data import MaritalStatusEnum
from services.risk_engine import ClassificationParams, InsuranceProfileEnum
from services.vehicle_insurance_engine import VehicleInsuranceEngine
from freezegun import freeze_time


class TestVehicleInsuranceEngine:
    @freeze_time("2022-03-01")
    @pytest.mark.parametrize(
        "personal_data__age, personal_data__income, vehicle_data__year, expected_profile",
        [
            (
                20,
                250_000,
                2021,
                InsuranceProfileEnum.ECONOMIC,
            ),
            (
                50,
                50_000,
                2000,
                InsuranceProfileEnum.REGULAR,
            ),
            (
                50,
                250_000,
                2021,
                InsuranceProfileEnum.REGULAR,
            ),
        ],
    )
    def test_when_valid_data__should_calculate_profile_correctly(
        self, classification_params: ClassificationParams, expected_profile: str
    ):
        life_insurance_engine = VehicleInsuranceEngine()
        profile = life_insurance_engine.determine_profile(
            classification_params=classification_params
        )

        assert profile == expected_profile
