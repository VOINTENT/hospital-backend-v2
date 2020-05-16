from typing import Any, List

from .service import Service
from .cabinet import Cabinet
from .abstract_model import AbstractModel
from .account import Account
from .speciality import Speciality
from .department import Department


class Doctor(AbstractModel):

    def __init__(self, id: int = None, created_at: Any = None, account: Account = None, first_name: str = None,
                 last_name: str = None, middle_name: str = None, gender: int = None, birth_date: Any = None,
                 speciality: Speciality = None, department: Department = None, cabinets: List[Cabinet] = None,
                 services: List[Service] = None) -> None:

        super().__init__(id, created_at)
        self.account = account
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
        self.birth_date = birth_date
        self.speciality = speciality
        self.department = department
        self.cabinets = cabinets
        self.services = services
