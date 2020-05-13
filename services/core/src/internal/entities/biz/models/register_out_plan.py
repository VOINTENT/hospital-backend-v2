from typing import Any

from .reception_plan import ReceptionPlan
from .patient import Patient
from .abstract_model import AbstractModel


class RegisterOutPlan(AbstractModel):

    def __init__(self, id: int, created_at: Any, reception_plan: ReceptionPlan, patient: Patient, time: Any) -> None:
        super().__init__(id, created_at)
        self.reception_plan = reception_plan
        self.patient = patient
        self.time = time
