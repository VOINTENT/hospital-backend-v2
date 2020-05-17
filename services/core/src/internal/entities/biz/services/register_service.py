from src.internal.entities.biz.dao.postgre.patient_dao import PatientDaoImpl
from src.internal.entities.biz.dao.postgre.register_dao import RegisterDaoImpl
from src.internal.entities.biz.models.register import Register
from src.internal.entities.biz.services.interfaces.register_service import RegisterService
from src.internal.errors.register import RECEPTION_LINE_BUSY


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

        return register_dao.add(register)
