import datetime

from src.internal.entities.biz.models.account import Account

# TODO Вынести куда-нибдудь
from src.internal.entities.biz.models.patient import Patient

COMMON = 'common'
ONLY_ID = 'only_id'


class PatientSerializer:

    def serialize(self, patient: Patient, format=COMMON) -> dict:
        serializer = self._get_serializer(format)
        return serializer(patient)

    def _get_serializer(self, format):
        if format == COMMON:
            return self._common_serialize
        elif format == ONLY_ID:
            return self._only_id_serialize

    @staticmethod
    def _common_serialize(patient: Patient):
        birth_date = None
        if patient.birth_date:
            day = str(patient.birth_date.date().day)
            month = str(patient.birth_date.date().month)
            year = str(patient.birth_date.date().year)
            birth_date = day + '-' + month + '-' + year

        if patient.gender is None:
            patient.gender = 3

        return {
            'user_id': patient.account.id,
            'patient_id': patient.id,
            'first_name': patient.first_name,
            'last_name': patient.last_name,
            'middle_name': patient.middle_name,
            'gender': patient.gender,
            'birth_date': birth_date,
            'snils': patient.snils,
            'policy': patient.policy,
            'email': patient.account.email,
            'phone_number': patient.account.phone_number
        }

    @staticmethod
    def _only_id_serialize(account: Account):

        return {
            'id': account.id
        }
