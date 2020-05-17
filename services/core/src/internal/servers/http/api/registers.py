from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.deserializers.register_deserializer import RegisterDeserializer, COMMON
from src.internal.entities.biz.serializers.register_serializer import RegisterSerializer
from src.internal.entities.biz.services.register_service import RegisterServiceImpl
from src.internal.entities.biz.validators.register import RegisterSchema
from src.internal.errors.common import NOT_AUTHORIZED, NOT_VALID_TOKEN, OK
from src.internal.servers.http.answer import get_response, get_response_with_validation_mistakes
from src.lib.utils.utls import get_payload

registers = Blueprint('registers', url_prefix='/registers')


@registers.route('/', methods=['POST', 'GET'])
def register(request):

    if request.method == 'POST':
        token = request.cookies.get('token')
        if not token:
            return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 401)

        payload = get_payload(token)
        if not payload:
            return json(get_response(NOT_VALID_TOKEN[0], NOT_VALID_TOKEN[1]), 401)
        account_id = payload['id']

        data = request.form
        mistakes = RegisterSchema().validate(data)
        if mistakes:
            return json(get_response_with_validation_mistakes(mistakes), 400)

        register = RegisterDeserializer.deserialize(data, COMMON)
        register.patient.account.id = account_id
        register, err = RegisterServiceImpl.add(register)
        if err:
            return json(get_response(err[0], err[1]), 400)

        return json(get_response(OK[0], OK[1]))

    elif request.method == 'GET':
        token = request.cookies.get('token')
        if not token:
            return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 401)

        payload = get_payload(token)
        if not payload:
            return json(get_response(NOT_VALID_TOKEN[0], NOT_VALID_TOKEN[1]), 401)
        account_id = payload['id']

        registers, err = RegisterServiceImpl.get_all_by_account_id(account_id)
        if err:
            return json(get_response(err[0], err[1]), 400)

        register_serializer = RegisterSerializer()
        resp_data = [register_serializer.serialize(register, COMMON) for register in registers]

        return json(get_response(OK[0], OK[1], data=resp_data))


@registers.route('/<register_id>', methods=['DELETE'])
def register_delete(request, register_id):
    token = request.cookies.get('token')
    if not token:
        return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 401)

    payload = get_payload(token)
    if not payload:
        return json(get_response(NOT_VALID_TOKEN[0], NOT_VALID_TOKEN[1]), 401)
    account_id = payload['id']

    register, err = RegisterServiceImpl.delete_my_register(register_id, account_id)
    if err:
        return json(get_response(err[0], err[1]), 400)

    return json(get_response(OK[0], OK[1]))
