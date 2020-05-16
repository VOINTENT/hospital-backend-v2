from src.internal.entities.biz.models.patient import Patient


class PatientService:
    """
    Класс является интерфейсом для методов работы с бизнес-логикой
    Каждый такой интерфейс должен наследоваться и реализовываться классом из пакета services
    """

    @staticmethod
    def signup(patient: Patient):
        raise NotImplemented

    @staticmethod
    def get_by_account_id(account_id: int) -> Patient or None:
        raise NotImplemented

    @staticmethod
    def update(patient: Patient):
        raise NotImplemented