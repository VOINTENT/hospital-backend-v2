from typing import List

from src.internal.entities.biz.dao.postgre.service_category_dao import ServiceCategoryDaoImpl
from src.internal.entities.biz.models.service_category import ServiceCategory
from src.internal.entities.biz.services.interfaces.service_category_service import ServiceCategoryService


class ServiceCategoryServiceImpl(ServiceCategoryService):
    """
    Класс является реализацией интерфейса AccService
    Каждый такой класс должен наследоваться от одного из интерфейсов в пакете services.interfaces
    """

    @staticmethod
    def get_all() -> (List[ServiceCategory] or None, tuple or None):
        return ServiceCategoryDaoImpl().get_all()
