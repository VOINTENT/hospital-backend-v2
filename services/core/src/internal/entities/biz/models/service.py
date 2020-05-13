from typing import Any

from .department import Department
from .abstract_model import AbstractModel
from .account import Account


class Service(AbstractModel):

    def __init__(self, id: int, created_at: Any, number: str, department: Department) -> None:

        super().__init__(id, created_at)
        self._number = number
        self._department = department
