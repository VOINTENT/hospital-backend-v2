from src.internal.entities.biz.models.account import Account
from src.lib.utils.utls import get_hash
from .interfaces.account_service import AccountService
from src.internal.entities.biz.dao.postgre.account_dao import AccountDaoImpl


class AccountServiceImpl(AccountService):
    """
    Класс является реализацией интерфейса AccService
    Каждый такой класс должен наследоваться от одного из интерфейсов в пакете services.interfaces
    """
    @staticmethod
    def signup(account: Account):
        pass

    @staticmethod
    def login(account: Account):
        email_or_phone = account.email_or_phone_number
        hash_password = get_hash(account.password)
        return AccountDaoImpl().get_by_email_or_phone_number_and_password(email_or_phone, hash_password)
