from typing import Any

from .doctor import Doctor
from .service import Service
from .abstract_model import AbstractModel


class ReceptionPlan(AbstractModel):

    def __init__(self, id: int = None, created_at: Any = None, service: Service = None, doctor: Doctor = None, date: Any = None) -> None:
        super().__init__(id, created_at)
        self.service = service
        self.doctor = doctor
        self.date = date
