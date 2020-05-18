from typing import List

from src.internal.entities.biz.dao.postgre.reception_line_dao import ReceptionLineDaoImpl
from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.internal.entities.biz.services.interfaces.reception_line_service import ReceptionLineService


class ReceptionLineServiceImpl(ReceptionLineService):
    """
    Класс является реализацией интерфейса AccService
    Каждый такой класс должен наследоваться от одного из интерфейсов в пакете services.interfaces
    """

    @staticmethod
    def get_all_free_by_filter(filter: list) -> (List[ReceptionLine] or None, tuple or None):
        return ReceptionLineDaoImpl().get_all_free_by_filter(filter)
