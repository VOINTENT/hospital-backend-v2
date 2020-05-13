from .base_dao import BaseDao


class AccDao(BaseDao):
    """
    Данный класс является интерфейсом для всевозможных запросов к БД для конкретной модели (в данном случае Acc)
    Каждый такой интерфейс должен наследовать BaseDao
    """
    def __init__(self, db) -> None:
        super().__init__(db)
