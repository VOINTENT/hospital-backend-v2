from typing import Any

from .department import Department
from .abstract_model import AbstractModel
from .account import Account


class ServiceCategory(AbstractModel):

    def __init__(self, id: int, created_at: Any, name: str) -> None:

        super().__init__(id, created_at)
        self._name = name
