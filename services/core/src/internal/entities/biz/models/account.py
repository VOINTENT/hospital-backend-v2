from typing import Any

from .abstract_model import AbstractModel


class Account(AbstractModel):

    def __init__(self, id: int, created_at: Any, email: str, phone_number: str, password: str, is_active: bool,
                 user_type: str) -> None:

        super().__init__(id, created_at)
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.is_active = is_active
        self.user_Type = user_type
