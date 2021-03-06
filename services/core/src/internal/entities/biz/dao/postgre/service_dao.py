from typing import List

from src.internal.entities.biz.dao.interfaces.doctor_dao import DoctorDao
from src.internal.entities.biz.models.doctor import Doctor
from src.internal.entities.biz.models.service import Service
from src.internal.entities.biz.models.service_category import ServiceCategory


class ServiceDaoImpl(DoctorDao):
    """
    Данный класс является реализацией интерфейса AccDao, применимой для работы конкретно с PostgreSQL
    Каждый такой класс должен являться реализацией соответствующего интерфейса из пакета dao.interfaces
    """

    def get_all(self) -> (List[Service] or None, tuple or None):
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT id, name
            FROM service
            """)
            data = cur.fetchall()
            services = [Service(id=row[0], name=row[1]) for row in data]
            return services, None
