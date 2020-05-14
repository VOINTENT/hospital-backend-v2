from typing import Any

from .abstract_model import AbstractModel
from .account import Account


class Patient(AbstractModel):

    def __init__(self, id: int = None, created_at: Any = None, account: Account = None, first_name: str = None,
                 last_name: str = None, middle_name: str = None, gender: int = None, birth_date: Any = None,
                 snils: str = None, policy: str = None) -> None:

        super().__init__(id, created_at)
        self.account = account
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
        self.birth_date = birth_date
        self.snils = snils
        self.policy = policy
