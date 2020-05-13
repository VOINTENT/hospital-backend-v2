from ..interfaces.account_dao import AccDao
from src.internal.entities.biz.models.account import Acc


class AccDaoImpl(AccDao):
    """
    Данный класс является реализацией интерфейса AccDao, применимой для работы конкретно с PostgreSQL
    Каждый такой класс должен являться реализацией соответствующего интерфейса из пакета dao.interfaces
    """

    def __init__(self, db) -> None:
        super().__init__(db)

    def get_by_id(self, id: int) -> (Acc, bool):
        pass

    def add(self, acc: Acc) -> (None, bool):
        pass

    def remove(self, acc: Acc) -> (None, bool):
        pass

    def remove_by_id(self, id: int) -> (None, bool):
        pass

    def get_all(self) -> (list, bool):
        pass

    def get_by_username(self, username: str):
        pass
