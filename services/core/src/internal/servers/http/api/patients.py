from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.serializers.patient_serializer import PatientSerializer, COMMON
from src.internal.entities.biz.services.patient_service import PatientServiceImpl
from src.internal.errors.common import NOT_AUTHORIZED, NOT_VALID_TOKEN, OK
from src.internal.servers.http.answer import get_response
from src.lib.utils.utls import get_payload
from .auth import auth

patients_loc = Blueprint('patients', url_prefix='')
patients = Blueprint.group(auth, patients_loc, url_prefix='/patients')


@patients_loc.route('/')
async def patient_detail(request):
    token = request.cookies.get('token')
    if not token:
        return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 401)

    payload = get_payload(token)
    if not payload:
        return json(get_response(NOT_VALID_TOKEN[0], NOT_VALID_TOKEN[1]), 401)

    account_id = payload['id']
    patient, err = PatientServiceImpl.get_by_account_id(account_id)
    if err:
        return json(get_response(err[0], err[1]), 400)

    resp_data = PatientSerializer().serialize(patient, COMMON)

    return json(get_response(OK[0], OK[1], data=resp_data))
