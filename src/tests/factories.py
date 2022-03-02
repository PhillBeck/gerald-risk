from factory import DictFactory, Factory, SubFactory
from models import PersonalData, HouseData, VehicleData
from services.risk_engine import ClassificationParams


class ApiPayloadFactory(DictFactory):
    age = 35
    dependents = 1
    income = 100_000
    marital_status = "single"
    risk_questions = [1, 0, 0]
    house = {"ownership_status": "owned"}
    vehicle = None


class PersonalDataFactory(Factory):
    class Meta:
        model = PersonalData

    age = 35
    dependents = 1
    income = 100_000
    marital_status = "single"
    risk_questions = [1, 0, 0]


class HouseDataFactory(Factory):
    class Meta:
        model = HouseData

    ownership_status = "owned"


class VehicleDataFactory(Factory):
    class Meta:
        model = VehicleData

    year = 2020


class ClassificationParamsFactory(Factory):
    class Meta:
        model = ClassificationParams

    personal_data = SubFactory(PersonalDataFactory)
    house_data = SubFactory(HouseDataFactory)
    vehicle_data = SubFactory(VehicleDataFactory)
