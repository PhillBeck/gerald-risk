import pytest
from models.house_data import HouseOwnershipStatusEnum
from models.personal_data import MaritalStatusEnum
from services.disability_insurance_engine import DisabilityInsuranceEngine
from services.risk_engine import ClassificationParams, InsuranceProfileEnum


class TestDisabilityInsuranceEngine:
    @pytest.mark.parametrize(
        "personal_data__age, personal_data__marital_status, personal_data__dependents, house_data__ownership_status, expected_profile",
        [
            (
                35,
                MaritalStatusEnum.SINGLE,
                1,
                HouseOwnershipStatusEnum.OWNED,
                InsuranceProfileEnum.REGULAR,
            ),
            (
                20,
                MaritalStatusEnum.SINGLE,
                0,
                HouseOwnershipStatusEnum.OWNED,
                InsuranceProfileEnum.ECONOMIC,
            ),
            (
                65,
                MaritalStatusEnum.SINGLE,
                1,
                HouseOwnershipStatusEnum.OWNED,
                InsuranceProfileEnum.INELIGIBLE,
            ),
            (
                50,
                MaritalStatusEnum.SINGLE,
                2,
                HouseOwnershipStatusEnum.OWNED,
                InsuranceProfileEnum.REGULAR,
            ),
            (
                50,
                MaritalStatusEnum.SINGLE,
                1,
                HouseOwnershipStatusEnum.MORTGAGED,
                InsuranceProfileEnum.RESPONSIBLE,
            ),
        ],
    )
    def test_when_valid_data__should_calculate_profile_correctly(
        self, classification_params: ClassificationParams, expected_profile: str
    ):
        life_insurance_engine = DisabilityInsuranceEngine()
        profile = life_insurance_engine.determine_profile(
            classification_params=classification_params
        )

        assert profile == expected_profile
