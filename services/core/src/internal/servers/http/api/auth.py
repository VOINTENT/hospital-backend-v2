from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.deserializers.patient_deserializer import PatientDeserializer, SIGNUP_TYPE
from src.internal.entities.biz.serializers.account_serializer import COMMON
from src.internal.entities.biz.serializers.patient_serializer import PatientSerializer
from src.internal.entities.biz.services.patient_service import PatientServiceImpl
from src.internal.entities.biz.validators.login import LoginSchema
from src.internal.entities.biz.validators.signup import SignupSchema
from src.internal.errors.common import OK, NOT_AUTHORIZED
from src.internal.servers.http.answer import get_response
from src.internal.servers.http.answer import get_response_with_validation_mistakes
from src.internal.entities.biz.deserializers.account_deserializer import AccountDeserializer, LOGIN_TYPE
from src.internal.entities.biz.services.account_service import AccountServiceImpl
from src.lib.utils.utls import get_token

auth = Blueprint('auth', url_prefix='/auth')


@auth.route('/login/basic', methods=['POST'])
async def patient_login(request):
    data = request.form

    mistakes = LoginSchema().validate(data)
    if mistakes:
        return json(get_response_with_validation_mistakes(mistakes), 400)

    account = AccountDeserializer.deserialize(data, LOGIN_TYPE)
    patient, err = AccountServiceImpl.login(account)
    if err:
        return json(get_response(err[0], err[1]), 400)

    resp_data = PatientSerializer().serialize(patient, COMMON)

    resp = json(get_response(OK[0], OK[1], resp_data))
    resp.cookies['token'] = get_token(patient.account)
    return resp


@auth.route('/signup', methods=['POST'])
async def patient_signup(request):
    data = request.form

    mistakes = SignupSchema().validate(data)
    if mistakes:
        return json(get_response_with_validation_mistakes(mistakes), 400)

    patient = PatientDeserializer.deserialize(data, SIGNUP_TYPE)
    patient, err = PatientServiceImpl.signup(patient)
    if err:
        return json(get_response(err[0], err[1]), 400)

    resp_data = PatientSerializer().serialize(patient, COMMON)
    resp = json(get_response(OK[0], OK[1], data=resp_data))
    resp.cookies['token'] = get_token(patient.account)
    return resp


@auth.route('/logout', methods=['DELETE'])
async def patient_logout(request):
    token = request.cookies.get('token')
    if not token:
        return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 400)

    resp = json(get_response(OK[0], OK[1]))
    del resp.cookies['token']
    return resp


@auth.route('/restore-password', methods=['POST'])
async def patient_restore_password(request):
    return json(get_response(OK[0], OK[1]))
