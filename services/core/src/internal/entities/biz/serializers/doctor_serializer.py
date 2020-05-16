from src.internal.entities.biz.models.doctor import Doctor

FOR_FILTER = 'for-filter'


class DoctorSerializer:

    def serialize(self, doctor: Doctor, format) -> dict:
        serializer = self._get_serializer(format)
        return serializer(doctor)

    def _get_serializer(self, format):
        if format == FOR_FILTER:
            return self._for_filter_serialize

    @staticmethod
    def _for_filter_serialize(doctor: Doctor):
        return {
            'id': doctor.id,
            'first_name': doctor.first_name,
            'last_name': doctor.last_name,
            'middle_name': doctor.middle_name
        }