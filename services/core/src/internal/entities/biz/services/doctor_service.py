from typing import List

from src.internal.entities.biz.dao.postgre.doctor_dao import DoctorDaoImpl
from src.internal.entities.biz.models.doctor import Doctor
from src.internal.entities.biz.services.interfaces.doctor_service import DoctorService


class DoctorServiceImpl(DoctorService):
    """
    Класс является реализацией интерфейса AccService
    Каждый такой класс должен наследоваться от одного из интерфейсов в пакете services.interfaces
    """

    @staticmethod
    def get_all() -> (List[Doctor] or None, tuple or None):
        return DoctorDaoImpl().get_all()
