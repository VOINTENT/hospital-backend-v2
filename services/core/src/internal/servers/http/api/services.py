from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.serializers.service_category_serializer import ServiceCategorySerializer, FOR_FILTER
from src.internal.entities.biz.serializers.service_serializer import ServiceSerializer
from src.internal.entities.biz.services.service_category_service import ServiceCategoryServiceImpl
from src.internal.entities.biz.services.service_service import ServiceServiceImpl
from src.internal.errors.common import NOT_AUTHORIZED, NOT_VALID_TOKEN, OK
from src.internal.servers.http.answer import get_response
from src.lib.utils.utls import get_payload

services = Blueprint('services', url_prefix='/services')


@services.route('/')
def get_all_services(request):
    token = request.cookies.get('token')
    if not token:
        return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 401)

    payload = get_payload(token)
    if not payload:
        return json(get_response(NOT_VALID_TOKEN[0], NOT_VALID_TOKEN[1]), 401)

    services, err = ServiceServiceImpl.get_all()
    if err:
        return json(get_response(err[0], err[1]), 400)

    service_serializer = ServiceSerializer()
    resp_data = [service_serializer.serialize(service, FOR_FILTER) for service in services]

    return json(get_response(OK[0], OK[1], data=resp_data))
