from typing import Any

from .abstract_model import AbstractModel
from .account import Account


class Patient(AbstractModel):

    def __init__(self, id: int, created_at: Any, account: Account, first_name: str, last_name: str, middle_name: str,
                 gender: int, birth_date: Any, snils: str, policy: str) -> None:

        super().__init__(id, created_at)
        self.account = account
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
        self.birth_date = birth_date
        self.snils = snils
        self.policy = policy
