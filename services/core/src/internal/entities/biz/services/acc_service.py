from src.internal.entities.biz.models.account import Acc
from .interfaces.acc_service import AccService


class AccServiceImpl(AccService):
    """
    Класс является реализацией интерфейса AccService
    Каждый такой класс должен наследоваться от одного из интерфейсов в пакете services.interfaces
    """
    @staticmethod
    def signup(acc: Acc):
        pass

    @staticmethod
    def login(acc: Acc):
        pass