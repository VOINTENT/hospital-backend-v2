from src.internal.entities.biz.models.service_category import ServiceCategory

FOR_FILTER = 'for-filter'


class ServiceCategorySerializer:

    def serialize(self, service_category: ServiceCategory, format) -> dict:
        serializer = self._get_serializer(format)
        return serializer(service_category)

    def _get_serializer(self, format):
        if format == FOR_FILTER:
            return self._for_filter_serialize

    @staticmethod
    def _for_filter_serialize(service_category: ServiceCategory):
        return {
            'id': service_category.id,
            'name': service_category.name,
        }
