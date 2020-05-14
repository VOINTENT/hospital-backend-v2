from src.internal.entities.biz.models.account import Account

# TODO Вынести куда-нибдудь
COMMON = 'common'
ONLY_ID = 'only_id'


class AccountSerializer:

    def serialize(self, account: Account, format=COMMON) -> dict:
        serializer = self._get_serializer(format)
        return serializer(account)

    def _get_serializer(self, format):
        if format == COMMON:
            return self._common_serialize
        elif format == ONLY_ID:
            return self._only_id_serialize

    @staticmethod
    def _common_serialize(account: Account):
        return {
            'id': account.id,
        }

    @staticmethod
    def _only_id_serialize(account: Account):
        return {
            'id': account.id
        }
