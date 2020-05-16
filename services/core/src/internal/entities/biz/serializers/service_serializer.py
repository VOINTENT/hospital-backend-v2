from src.internal.entities.biz.models.service import Service

FOR_FILTER = 'for-filter'


class ServiceSerializer:

    def serialize(self, service: Service, format) -> dict:
        serializer = self._get_serializer(format)
        return serializer(service)

    def _get_serializer(self, format):
        if format == FOR_FILTER:
            return self._for_filter_serialize

    @staticmethod
    def _for_filter_serialize(service: Service):
        return {
            'id': service.id,
            'name': service.name,
        }
