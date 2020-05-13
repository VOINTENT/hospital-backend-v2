from typing import Any, List

from .service import Service
from .cabinet import Cabinet
from .abstract_model import AbstractModel
from .account import Account
from .speciality import Speciality
from .department import Department


class Doctor(AbstractModel):

    def __init__(self, id: int, created_at: Any, account: Account, first_name: str, last_name: str, middle_name: str,
                 gender: int, birth_date: Any, speciality: Speciality, department: Department, cabinets: List[Cabinet],
                 services: List[Service]) -> None:

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
