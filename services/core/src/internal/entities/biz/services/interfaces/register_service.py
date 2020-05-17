from src.internal.entities.biz.models.register import Register


class RegisterService:
    """
    Класс является интерфейсом для методов работы с бизнес-логикой
    Каждый такой интерфейс должен наследоваться и реализовываться классом из пакета services
    """

    @staticmethod
    def add(register: Register) -> (Register or None, None or tuple):
        raise NotImplemented
