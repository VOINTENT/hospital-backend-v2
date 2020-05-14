from src.internal.entities.biz.models.account import Account

# TODO Вынести куда-нибдудь
LOGIN_TYPE = 'login'


class AccountDeserializer:

    @classmethod
    def deserialize(cls, account: dict, format=LOGIN_TYPE) -> Account:
        deserializer = cls._get_deserializer(format)
        return deserializer(account)

    @classmethod
    def _get_deserializer(cls, format):
        if format == LOGIN_TYPE:
            return cls._login_deserialize

    @staticmethod
    def _login_deserialize(account_dict: dict):
        return Account(
            email_or_phone_number=account_dict.get('email_or_phone'),
            password=account_dict.get('password')
        )
