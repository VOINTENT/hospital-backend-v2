# TODO Вынести куда-нибдудь
from src.internal.entities.biz.models.account import Account
from src.internal.entities.biz.models.patient import Patient
from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.internal.entities.biz.models.register import Register

COMMON = 'common'


class RegisterDeserializer:

    @classmethod
    def deserialize(cls, register: dict, format) -> Register:
        deserializer = cls._get_deserializer(format)
        return deserializer(register)

    @classmethod
    def _get_deserializer(cls, format):
        if format == COMMON:
            return cls._register_deserialize

    @staticmethod
    def _register_deserialize(register_dict: dict):
        return Register(
            reception_line=ReceptionLine(
                id=register_dict.get('reception_line_id')
            ),
            patient=Patient(
                account=Account()
            )
        )
