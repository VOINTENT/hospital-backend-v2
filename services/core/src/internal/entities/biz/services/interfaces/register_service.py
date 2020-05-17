from typing import List

from src.internal.entities.biz.models.register import Register


class RegisterService:
    """
    Класс является интерфейсом для методов работы с бизнес-логикой
    Каждый такой интерфейс должен наследоваться и реализовываться классом из пакета services
    """

    @staticmethod
    def add(register: Register) -> (Register or None, None or tuple):
        raise NotImplemented
    
    @staticmethod
    def get_all_by_account_id(patient_id: int) -> (List[Register] or None, None or tuple):
        raise NotImplemented

    @staticmethod
    def delete_my_register(register_id: int, account_id: int) -> (Register or None, None or tuple):
        raise NotImplemented
