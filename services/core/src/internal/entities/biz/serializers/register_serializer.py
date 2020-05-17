from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.internal.entities.biz.models.register import Register
from src.lib.utils.utls import serialize_date, serialize_time

COMMON = 'common'


class RegisterSerializer:

    def serialize(self, register: Register, format) -> dict:
        serializer = self._get_serializer(format)
        return serializer(register)

    def _get_serializer(self, format):
        if format == COMMON:
            return self._common_serialize

    @staticmethod
    def _common_serialize(register: Register):
        return {
            'id': register.id,
            'service': {
                'id': register.reception_line.reception_plan.service.id,
                'name': register.reception_line.reception_plan.service.name,
            },
            'service_category': {
                'id': register.reception_line.reception_plan.service.service_category.id,
                'name': register.reception_line.reception_plan.service.service_category.name
            },
            'doctor': {
                'id': register.reception_line.reception_plan.doctor.id,
                'first_name': register.reception_line.reception_plan.doctor.first_name,
                'last_name': register.reception_line.reception_plan.doctor.last_name,
                'middle_name': register.reception_line.reception_plan.doctor.middle_name
            },
            'date': serialize_date(register.reception_line.reception_plan.date),
            'time': serialize_time(register.reception_line.time)
        }
