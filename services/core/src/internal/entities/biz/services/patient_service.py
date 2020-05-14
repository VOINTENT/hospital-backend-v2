from src.internal.entities.biz.dao.postgre.patient_dao import PatientDaoImpl
from src.internal.entities.biz.models.account import Account
from src.internal.entities.biz.models.patient import Patient
from src.internal.entities.biz.services.interfaces.patient_service import PatientService
from src.internal.errors.common import DATABASE_MISTAKE
from src.internal.errors.signup import EMAIL_EXISTS, PHONE_NUMBER_EXISTS
from src.lib.utils.utls import get_hash
from .interfaces.account_service import AccountService
from src.internal.entities.biz.dao.postgre.account_dao import AccountDaoImpl


class PatientServiceImpl(PatientService):
    """
    Класс является реализацией интерфейса AccService
    Каждый такой класс должен наследоваться от одного из интерфейсов в пакете services.interfaces
    """
    @staticmethod
    def signup(patient: Patient) -> (Patient or None, tuple or None):
        account_dao = AccountDaoImpl()
        patient_dao = PatientDaoImpl()
        if account_dao.is_email_exists(patient.account.email):
            return None, EMAIL_EXISTS

        if account_dao.is_phone_number_exists(patient.account.phone_number):
            return None, PHONE_NUMBER_EXISTS

        patient.account.password = get_hash(patient.account.password)
        account, err = account_dao.add(patient.account)
        if err:
            return None, DATABASE_MISTAKE

        patient, err = patient_dao.add(patient)
        if err:
            return None, DATABASE_MISTAKE

        return patient, None
