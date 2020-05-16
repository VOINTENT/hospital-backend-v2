from src.internal.entities.biz.models.account import Account
from src.internal.entities.biz.models.patient import Patient

import datetime

SIGNUP_TYPE = 'signup'
EDIT_TYPE = 'edit'


class PatientDeserializer:

    @classmethod
    def deserialize(cls, patient_dict: dict, format) -> Patient:
        deserializer = cls._get_deserializer(format)
        return deserializer(patient_dict)

    @classmethod
    def _get_deserializer(cls, format):
        if format == SIGNUP_TYPE:
            return cls._signup_deserialize
        if format == EDIT_TYPE:
            return cls._edit_deserialize

    @staticmethod
    def _signup_deserialize(patient_dict: dict) -> Patient:
        return Patient(
            account=Account(
                phone_number=patient_dict.get('phone_number'),
                email=patient_dict.get('email'),
                password=patient_dict.get('password')
            ),
            last_name=patient_dict.get('last_name'),
            first_name=patient_dict.get('first_name'),
            middle_name=patient_dict.get('middle_name')
        )

    @staticmethod
    def _edit_deserialize(patient_dict) -> Patient:
        date = patient_dict.get('birth_date').split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])

        return Patient(
            account=Account(),
            last_name=patient_dict.get('last_name'),
            first_name=patient_dict.get('first_name'),
            middle_name=patient_dict.get('middle_name'),
            birth_date=datetime.date(year, month, day),
            gender=int(patient_dict.get('gender')),
            snils=patient_dict.get('snils'),
            policy=patient_dict.get('policy')
        )
