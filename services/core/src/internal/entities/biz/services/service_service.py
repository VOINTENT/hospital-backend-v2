from typing import List

from src.internal.entities.biz.dao.postgre.service_dao import ServiceDaoImpl
from src.internal.entities.biz.models.service import Service
from src.internal.entities.biz.services.interfaces.service_service import ServiceService


class ServiceServiceImpl(ServiceService):
    """
    Класс является реализацией интерфейса AccService
    Каждый такой класс должен наследоваться от одного из интерфейсов в пакете services.interfaces
    """

    @staticmethod
    def get_all() -> (List[Service] or None, tuple or None):
        return ServiceDaoImpl().get_all()
