from typing import Any

from .patient import Patient
from .reception_line import ReceptionLine
from .abstract_model import AbstractModel


class Register(AbstractModel):

    def __init__(self, id: int, created_at: Any, reception_line: ReceptionLine, patient: Patient) -> None:
        super().__init__(id, created_at)
        self.reception_line = reception_line
        self.patient = patient
