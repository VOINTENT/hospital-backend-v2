from typing import List

from src.internal.entities.biz.models.doctor import Doctor
from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.internal.entities.biz.models.service import Service
from src.internal.entities.biz.models.service_category import ServiceCategory


class ReceptionLineService:
    """
    Класс является интерфейсом для методов работы с бизнес-логикой
    Каждый такой интерфейс должен наследоваться и реализовываться классом из пакета services
    """

    @staticmethod
    def get_all_free_by_filter(filter: list) -> (List[ReceptionLine] or None, tuple or None):
        raise NotImplemented
