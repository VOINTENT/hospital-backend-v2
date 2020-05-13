from typing import Any

from src.internal.entities.biz.models.service import Service
from .abstract_model import AbstractModel


class Price(AbstractModel):

    def __init__(self, id: int, created_at: Any, service: Service, cost: float, date_approval: Any) -> None:
        super().__init__(id, created_at)
        self.service = service
        self.cost = cost
        self.date_approval = date_approval
