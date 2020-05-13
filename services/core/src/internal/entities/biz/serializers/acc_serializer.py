from src.internal.entities.biz.models.account import Acc

# TODO Вынести куда-нибдудь
COMMON = 'common'
ONLY_ID = 'only_id'


class AccSerializer:

    def serialize(self, acc: Acc, format=COMMON) -> dict:
        serializer = self._get_serializer(format)
        return serializer(acc)

    def deserialize(self, acc: dict) -> Acc:
        deserializer = self._get_deserializer()
        return deserializer(acc)

    def _get_serializer(self, format):
        if format == COMMON:
            return self._common_serialize
        elif format == ONLY_ID:
            return self._only_id_serialize

    def _get_deserializer(self):
        return self._from_dict_deserialize

    @staticmethod
    def _common_serialize(acc: Acc):
        return {
            'id': acc.id,
            'username': acc.username
        }

    @staticmethod
    def _only_id_serialize(acc: Acc):
        return {
            'id': acc.id
        }

    @staticmethod
    def _from_dict_deserialize(acc_dict: dict):
        return Acc(
            id=acc_dict.get('id'),
            username=acc_dict.get('username')
        )
