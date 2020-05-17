from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.deserializers.register_deserializer import RegisterDeserializer, COMMON
from src.internal.entities.biz.services.register_service import RegisterServiceImpl
from src.internal.entities.biz.validators.register import RegisterSchema
from src.internal.errors.common import NOT_AUTHORIZED, NOT_VALID_TOKEN, OK
from src.internal.servers.http.answer import get_response, get_response_with_validation_mistakes
from src.lib.utils.utls import get_payload

registers = Blueprint('registers', url_prefix='/registers')


@registers.route('/', methods=['POST'])
def add_register(request):
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
