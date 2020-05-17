import src.internal.instances.dbs as dbs


class BaseDao:
    """
    Данный класс является базовым интерфейсом для CRUD запросов к БД,
    пригодным для наследования другими интерфейсами или для реализации (лучше делать только первое)
    Интерфейс должен наследоваться всеми другими интерфейсами для каждой конкретной модели
    """

    def __init__(self) -> None:
        self.conn = dbs.main_pgsql_connect

    def get_by_id(self, obj_id: int) -> (object, bool):
        raise NotImplemented

    def add(self, obj: object) -> (None, bool):
        raise NotImplemented

    def update(self, obj) -> (object, bool):
        raise NotImplemented

    def remove(self, obj: object) -> (None, bool):
        raise NotImplemented

    def remove_by_id(self, obj_id: int) -> (None, bool):
        raise NotImplemented

    def get_all(self) -> (list, bool):
        raise NotImplemented
