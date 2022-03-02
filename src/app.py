from flask import Flask, request
from models import ResponseModel, RequestModel
from models import PersonalData

from services.life_insurance_engine import LifeInsuranceEngine
from services.vehicle_insurance_engine import VehicleInsuranceEngine
from services.home_insurance_engine import HomeInsuranceEngine
from services.disability_insurance_engine import DisabilityInsuranceEngine

from services.risk_engine import ClassificationParams, RiskService
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response

app = Flask("gerald_risk_api")
api = FlaskPydanticSpec("flask")

life_insurance_engine = LifeInsuranceEngine()
disability_insurance_engine = DisabilityInsuranceEngine()
home_insurance_engine = HomeInsuranceEngine()
vehicle_insurance_engine = VehicleInsuranceEngine()

risk_service = RiskService()
risk_service.register_engine("auto", vehicle_insurance_engine)
risk_service.register_engine("disability", disability_insurance_engine)
risk_service.register_engine("home", home_insurance_engine)
risk_service.register_engine("life", life_insurance_engine)


@app.route("/", methods=["POST"])
@api.validate(body=Request(RequestModel), resp=Response(HTTP_200=ResponseModel))
def define_insurance_profiles():
    body = RequestModel(**request.json)

    personal_data = PersonalData(**body.dict())
    house_data = body.house
    vehicle_data = body.vehicle

    classification_params = ClassificationParams(
        personal_data=personal_data, house_data=house_data, vehicle_data=vehicle_data
    )

    profiles = risk_service.determine_profiles(classification_params)
    response = ResponseModel(**profiles)
    return response.dict()


api.register(app)


if __name__ == "__main__":
    app.run()
