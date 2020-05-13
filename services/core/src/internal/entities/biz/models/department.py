from typing import Any

from .abstract_model import AbstractModel


class Department(AbstractModel):

    def __init__(self, id: int, created_at: Any, name: str) -> None:
        super().__init__(id, created_at)
        self.name = name
