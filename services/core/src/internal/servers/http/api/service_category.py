from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.serializers.doctor_serializer import DoctorSerializer, FOR_FILTER
from src.internal.entities.biz.services.doctor_service import DoctorServiceImpl
from src.internal.errors.common import NOT_AUTHORIZED, NOT_VALID_TOKEN, OK
from src.internal.servers.http.answer import get_response
from src.lib.utils.utls import get_payload

doctors = Blueprint('doctors', url_prefix='/doctors')


@doctors.route('/')
def get_all_service_categories(request):
    token = request.cookies.get('token')
    if not token:
        return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 401)

    payload = get_payload(token)
    if not payload:
        return json(get_response(NOT_VALID_TOKEN[0], NOT_VALID_TOKEN[1]), 401)

    service_categories, err = ServiceCategoryServiceImpl.get_all()
    if err:
        return json(get_response(err[0], err[1]), 400)

    resp_data = [ServiceCategory().serialize(service_categorie, FOR_FILTER) for service_categorie in service_categories]

    return json(get_response(OK[0], OK[1], data=resp_data))
