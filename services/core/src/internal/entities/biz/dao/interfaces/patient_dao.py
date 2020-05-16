from src.internal.entities.biz.models.patient import Patient
from .base_dao import BaseDao


class PatientDao(BaseDao):
    """
    Данный класс является интерфейсом для всевозможных запросов к БД для конкретной модели (в данном случае Acc)
    Каждый такой интерфейс должен наследовать BaseDao
    """

    def get_by_account_id(self, account_id: int) -> (Patient or None, bool):
        raise NotImplemented

    def is_policy_exists(self, policy: str) -> bool:
        raise NotImplemented

    def is_snils_exists(self, snils: str) -> bool:
        raise NotImplemented
