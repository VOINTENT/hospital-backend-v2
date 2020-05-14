from .base_dao import BaseDao


class AccountDao(BaseDao):
    """
    Данный класс является интерфейсом для всевозможных запросов к БД для конкретной модели (в данном случае Acc)
    Каждый такой интерфейс должен наследовать BaseDao
    """

    def get_by_email_or_phone_number_and_password(self, email_or_phone_number: str, password: str) -> (None, bool):
        raise NotImplemented

    def is_email_exists(self, email):
        raise NotImplemented

    def is_phone_number_exists(self, phone_number):
        raise NotImplemented
