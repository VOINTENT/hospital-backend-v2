from src.internal.entities.biz.models.account import Account


class AccountService:
    """
    Класс является интерфейсом для методов работы с бизнес-логикой
    Каждый такой интерфейс должен наследоваться и реализовываться классом из пакета services
    """

    @staticmethod
    def login(account: Account):
        raise NotImplemented
