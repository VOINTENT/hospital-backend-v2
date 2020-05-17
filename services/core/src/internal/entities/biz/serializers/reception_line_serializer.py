from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.lib.utils.utls import serialize_date, serialize_time

COMMON = 'common'


class ReceptionLineSerializer:

    def serialize(self, reception_line: ReceptionLine, format) -> dict:
        serializer = self._get_serializer(format)
        return serializer(reception_line)

    def _get_serializer(self, format):
        if format == COMMON:
            return self._common_serialize

    @staticmethod
    def _common_serialize(reception_line: ReceptionLine):
        return {
            'id': reception_line.id,
            'service': {
                'id': reception_line.reception_plan.service.id,
                'name': reception_line.reception_plan.service.name,
            },
            'service_category': {
                'id': reception_line.reception_plan.service.service_category.id,
                'name': reception_line.reception_plan.service.service_category.name
            },
            'doctor': {
                'id': reception_line.reception_plan.doctor.id,
                'first_name': reception_line.reception_plan.doctor.first_name,
                'last_name': reception_line.reception_plan.doctor.last_name,
                'middle_name': reception_line.reception_plan.doctor.middle_name
            },
            'date': serialize_date(reception_line.reception_plan.date),
            'time': serialize_time(reception_line.time)
        }
