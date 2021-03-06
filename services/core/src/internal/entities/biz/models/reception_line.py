from typing import Any

from src.internal.entities.biz.models.reception_plan import ReceptionPlan
from .doctor import Doctor
from .service import Service
from .abstract_model import AbstractModel


class ReceptionLine(AbstractModel):

    def __init__(self, id: int = None, created_at: Any = None, reception_plan: ReceptionPlan = None, time: Any = None) -> None:
        super().__init__(id, created_at)
        self.reception_plan = reception_plan
        self.time = time
