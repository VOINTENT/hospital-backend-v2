from typing import List

from src.internal.entities.biz.models.reception_line import ReceptionLine
from .base_dao import BaseDao


class ReceptionLineDao(BaseDao):
    """
    Данный класс является интерфейсом для всевозможных запросов к БД для конкретной модели (в данном случае Acc)
    Каждый такой интерфейс должен наследовать BaseDao
    """

    def get_all_free(self) -> (List[ReceptionLine], None or tuple):
        raise NotImplemented
