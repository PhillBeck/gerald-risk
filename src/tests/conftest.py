from pytest import fixture
from tests.factories import (
    ApiPayloadFactory,
    ClassificationParamsFactory,
    HouseDataFactory,
    PersonalDataFactory,
    VehicleDataFactory,
)

from pytest_factoryboy import register


@fixture
def api_payload(**kwargs):
    return ApiPayloadFactory(**kwargs)


register(PersonalDataFactory, "personal_data")
register(VehicleDataFactory, "vehicle_data")
register(HouseDataFactory, "house_data")


@fixture
def classification_params(personal_data, house_data, vehicle_data):
    return ClassificationParamsFactory(
        personal_data=personal_data, house_data=house_data, vehicle_data=vehicle_data
    )
