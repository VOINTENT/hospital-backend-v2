from typing import List

from src.internal.entities.biz.dao.postgre.patient_dao import PatientDaoImpl
from src.internal.entities.biz.dao.postgre.register_dao import RegisterDaoImpl
from src.internal.entities.biz.models.register import Register
from src.internal.entities.biz.services.interfaces.register_service import RegisterService
from src.internal.errors.register import RECEPTION_LINE_BUSY, NOT_AWAILABLE_REGISTER, TOO_MANY_REGISTERS


class RegisterServiceImpl(RegisterService):
    """
    Класс является реализацией интерфейса AccService
    Каждый такой класс должен наследоваться от одного из интерфейсов в пакете services.interfaces
    """

    @staticmethod
    def add(register: Register) -> (Register or None, None or tuple):
        patient_dao = PatientDaoImpl()
        register_dao = RegisterDaoImpl()

        register.patient, _ = patient_dao.get_by_account_id(register.patient.account.id)

        if register_dao.is_reception_line_busy(register.reception_line):
            return None, RECEPTION_LINE_BUSY

        if register_dao.is_patient_has_too_many_registers(register.patient.id):
            return None, TOO_MANY_REGISTERS

        return register_dao.add(register)

    @staticmethod
    def get_all_by_account_id(account_id: int) -> (List[Register] or None, None or tuple):
        patient_dao = PatientDaoImpl()
        register_dao = RegisterDaoImpl()

        patient, _ = patient_dao.get_by_account_id(account_id)

        return register_dao.get_all_by_patient_id(patient.id)

    @staticmethod
    def delete_my_register(register_id: int, account_id: int) -> (Register or None, None or tuple):
        patient_dao = PatientDaoImpl()
        register_dao = RegisterDaoImpl()

        patient, _ = patient_dao.get_by_account_id(account_id)

        if not register_dao.is_register_own_patient(register_id, patient.id):
            return None, NOT_AWAILABLE_REGISTER

        return register_dao.remove_by_id(register_id)
