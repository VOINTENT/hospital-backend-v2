from src.internal.entities.biz.models.reception_line import ReceptionLine
from .base_dao import BaseDao


class RegisterDao(BaseDao):
    """
    Данный класс является интерфейсом для всевозможных запросов к БД для конкретной модели (в данном случае Acc)
    Каждый такой интерфейс должен наследовать BaseDao
    """

    def is_reception_line_busy(self, reception_line: ReceptionLine) -> bool:
        raise NotImplemented

