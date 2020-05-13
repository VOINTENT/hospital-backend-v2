from src.internal.entities.biz.models.account import Acc


class AccService:
    """
    Класс является интерфейсом для методов работы с бизнес-логикой
    Каждый такой интерфейс должен наследоваться и реализовываться классом из пакета services
    """

    @staticmethod
    def signup(acc: Acc):
        raise NotImplemented

    @staticmethod
    def login(acc: Acc):
        raise NotImplemented
