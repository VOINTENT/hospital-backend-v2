from typing import List

from src.internal.entities.biz.models.doctor import Doctor


class DoctorService:
    """
    Класс является интерфейсом для методов работы с бизнес-логикой
    Каждый такой интерфейс должен наследоваться и реализовываться классом из пакета services
    """

    @staticmethod
    def get_all() -> (List[Doctor] or None, tuple or None):
        raise NotImplemented
