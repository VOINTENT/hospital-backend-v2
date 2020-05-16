from typing import Any

from src.internal.entities.biz.models.service_category import ServiceCategory
from .department import Department
from .abstract_model import AbstractModel
from .account import Account


class Service(AbstractModel):

    def __init__(self, id: int = None, created_at: Any = None, name: str = None, service_category: ServiceCategory = None) -> None:

        super().__init__(id, created_at)
        self.name = name
        self.service_category = service_category
