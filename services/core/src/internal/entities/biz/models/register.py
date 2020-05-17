from typing import Any

from .patient import Patient
from .reception_line import ReceptionLine
from .abstract_model import AbstractModel


class Register(AbstractModel):

    def __init__(self, id: int = None, created_at: Any = None, reception_line: ReceptionLine = None, patient: Patient = None) -> None:
        super().__init__(id, created_at)
        self.reception_line = reception_line
        self.patient = patient
