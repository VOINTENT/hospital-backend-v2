from typing import Any

from .abstract_model import AbstractModel


class Account(AbstractModel):

    def __init__(self, id: int or None = None, created_at: Any = None, email: str or None = None,
                 phone_number: str or None = None, password: str or None = None, is_active: bool or None = None,
                 user_type: str or None = None, email_or_phone_number: str or None = None) -> None:

        super().__init__(id, created_at)
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.is_active = is_active
        self.user_Type = user_type
        self.email_or_phone_number = email_or_phone_number
