from typing import List

from src.internal.entities.biz.dao.interfaces.doctor_dao import DoctorDao
from src.internal.entities.biz.models.doctor import Doctor


class DoctorDaoImpl(DoctorDao):
    """
    Данный класс является реализацией интерфейса AccDao, применимой для работы конкретно с PostgreSQL
    Каждый такой класс должен являться реализацией соответствующего интерфейса из пакета dao.interfaces
    """

    def get_all(self) -> (List[Doctor] or None, tuple or None):
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT id, first_name, last_name, middle_name
            FROM doctor
            """)
            data = cur.fetchall()
            patients = [Doctor(id=row[0], first_name=row[1], last_name=row[2], middle_name=row[3]) for row in data]
            return patients, None
