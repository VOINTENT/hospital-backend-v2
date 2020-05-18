from typing import List

from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.internal.entities.biz.models.register import Register
from .base_dao import BaseDao


class RegisterDao(BaseDao):
    """
    Данный класс является интерфейсом для всевозможных запросов к БД для конкретной модели (в данном случае Acc)
    Каждый такой интерфейс должен наследовать BaseDao
    """

    def is_reception_line_busy(self, reception_line: ReceptionLine) -> bool:
        raise NotImplemented

    def get_all_by_patient_id(self, patient_id: int) -> (List[Register] or None, None or tuple):
        raise NotImplemented

    def is_register_own_patient(self, register_id: int, patient_id: int) -> bool:
        raise NotImplemented

    def is_patient_has_too_many_registers(self, patient_id: int) -> bool:
        raise NotImplemented
