from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.serializers.reception_line_serializer import ReceptionLineSerializer, COMMON
from src.internal.entities.biz.services.reception_line_service import ReceptionLineServiceImpl
from src.internal.errors.common import NOT_AUTHORIZED, NOT_VALID_TOKEN, OK
from src.internal.servers.http.answer import get_response
from src.lib.utils.utls import get_payload

reception_lines = Blueprint('reception_lines', url_prefix='/reception-lines')


@reception_lines.route('/')
def get_all_free_reception_lines(request):
    token = request.cookies.get('token')
    if not token:
        return json(get_response(NOT_AUTHORIZED[0], NOT_AUTHORIZED[1]), 401)

    payload = get_payload(token)
    if not payload:
        return json(get_response(NOT_VALID_TOKEN[0], NOT_VALID_TOKEN[1]), 401)

    args = request.args
    filter = []
    if args.get('doctor_id') and args.get('doctor_id').isdigit():
        filter.append(('doctor.id = ', int(args.get('doctor_id'))))

    if args.get('service_id') and args.get('service_id').isdigit():
        filter.append(('service.id = ', int(args.get('service_id'))))

    if args.get('service_category_id') and args.get('service_category_id').isdigit():
        filter.append(('service_category.id = ', int(args.get('service_category_id'))))

    if args.get('date_start'):
        filter.append(('date >= ', args.get('date_start')))

    if args.get('date_finish'):
        filter.append(('date <= ', args.get('date_finish')))

    if args.get('time_start'):
        filter.append(('time >= ', args.get('time_start')))

    if args.get('time_finish'):
        filter.append(('time <= ', args.get('time_finish')))


    reception_lines, err = ReceptionLineServiceImpl.get_all_free_by_filter(filter)
    if err:
        return json(get_response(err[0], err[1]), 400)

    reception_line_serializer = ReceptionLineSerializer()
    resp_data = [reception_line_serializer.serialize(reception_line, COMMON) for reception_line in reception_lines]

    return json(get_response(OK[0], OK[1], data=resp_data))
