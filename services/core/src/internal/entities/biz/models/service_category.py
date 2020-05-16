from typing import Any

from .department import Department
from .abstract_model import AbstractModel
from .account import Account


class ServiceCategory(AbstractModel):

    def __init__(self, id: int = None, created_at: Any = None, name: str = None) -> None:
        super().__init__(id, created_at)
        self.name = name
