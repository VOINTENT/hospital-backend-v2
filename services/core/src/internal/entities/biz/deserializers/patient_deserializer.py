from src.internal.entities.biz.models.account import Account
from src.internal.entities.biz.models.patient import Patient

SIGNUP_TYPE = 'signup'


class PatientDeserializer:

    @classmethod
    def deserialize(cls, patient_dict: dict, format=SIGNUP_TYPE) -> Patient:
        deserializer = cls._get_deserializer(format)
        return deserializer(patient_dict)

    @classmethod
    def _get_deserializer(cls, format):
        if format == SIGNUP_TYPE:
            return cls._signup_deserialize

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
