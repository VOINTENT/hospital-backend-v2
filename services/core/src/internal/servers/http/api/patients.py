from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.deserializers.patient_deserializer import PatientDeserializer, EDIT_TYPE
from src.internal.entities.biz.serializers.patient_serializer import PatientSerializer, COMMON
from src.internal.entities.biz.services.patient_service import PatientServiceImpl
from src.internal.entities.biz.validators.patient_edit import PatientEditSchema
from src.internal.errors.common import NOT_AUTHORIZED, NOT_VALID_TOKEN, OK
from src.internal.servers.http.answer import get_response, get_response_with_validation_mistakes, \
    get_response_with_edit_fields
from src.lib.utils.utls import get_payload
from .auth import auth

patients_loc = Blueprint('patients', url_prefix='')
patients = Blueprint.group(auth, patients_loc, url_prefix='/patients')


@patients_loc.route('/', methods=['PATCH', 'GET', 'OPTIONS'])
async def patient(request):

    if request.method == 'GET':
        return patient_detail(request)
    elif request.method == 'PATCH':
        return patient_update(request)


def patient_detail(request):
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


def patient_update(request):
    token = request.cookies.get('token')
    if not token:
        return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 401)

    payload = get_payload(token)
    if not payload:
        return json(get_response(NOT_VALID_TOKEN[0], NOT_VALID_TOKEN[1]), 401)

    account_id = payload['id']

    data = request.form

    mistakes = PatientEditSchema().validate(data)
    if mistakes:
        return json(get_response_with_validation_mistakes(mistakes), 400)

    patient = PatientDeserializer.deserialize(data, EDIT_TYPE)
    patient.account.id = account_id

    patient, err = PatientServiceImpl.update(patient)
    if err:
        return json(get_response(err[0], err[1]), 400)

    return json(get_response_with_edit_fields(OK[0], OK[1], list(data.keys())))
