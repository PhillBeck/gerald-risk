from models.personal_data import PersonalData
from pydantic import ValidationError
import pytest
from ..factories import ApiPayloadFactory

from models.request import RequestModel


class TestRequestModel:
    def test_when_age_negative__should_raise_exception(self):
        api_payload = ApiPayloadFactory(age=-1)
        with pytest.raises(ValidationError):
            personal_data = PersonalData(**api_payload)

    def test_when_dependents_negative__should_raise_exception(self):
        api_payload = ApiPayloadFactory(dependents=-1)
        with pytest.raises(ValidationError):
            personal_data = PersonalData(**api_payload)

    def test_when_risk_questions_has_2_elems__should_raise_exception(self):
        api_payload = ApiPayloadFactory(risk_questions=[1, 1])
        with pytest.raises(ValidationError):
            personal_data = PersonalData(**api_payload)

    def test_when_risk_questions_has_invalid_elems__should_raise_exception(self):
        api_payload = ApiPayloadFactory(risk_questions=[3, 1, -1])
        with pytest.raises(ValidationError):
            personal_data = PersonalData(**api_payload)

    def test_when_valid_payload__should_validate_without_errors(self):
        api_payload = ApiPayloadFactory()
        personal_data = RequestModel(**api_payload)
        assert personal_data.age == api_payload["age"]
        assert personal_data.dependents == api_payload["dependents"]
        assert personal_data.marital_status == api_payload["marital_status"]
        assert personal_data.income == api_payload["income"]
        assert (
            personal_data.house.ownership_status
            == api_payload["house"]["ownership_status"]
        )
