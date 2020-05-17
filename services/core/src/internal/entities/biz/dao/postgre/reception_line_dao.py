from typing import List

from src.internal.entities.biz.dao.interfaces.doctor_dao import DoctorDao
from src.internal.entities.biz.dao.interfaces.reception_line_dao import ReceptionLineDao
from src.internal.entities.biz.models.doctor import Doctor
from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.internal.entities.biz.models.reception_plan import ReceptionPlan
from src.internal.entities.biz.models.service import Service
from src.internal.entities.biz.models.service_category import ServiceCategory


class ReceptionLineDaoImpl(ReceptionLineDao):
    """
    Данный класс является реализацией интерфейса AccDao, применимой для работы конкретно с PostgreSQL
    Каждый такой класс должен являться реализацией соответствующего интерфейса из пакета dao.interfaces
    """

    def get_all_free(self) -> (List[ReceptionLine], None or tuple):
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT reception_line.id, service.id, service.name, service_category.id, service_category.name, doctor.id, first_name, last_name, middle_name, date, time
            FROM reception_line 
                INNER JOIN reception_plan ON reception_line.id = reception_plan.id 
                INNER JOIN service ON reception_plan.service_id = service.id
                INNER JOIN doctor ON reception_plan.doctor_id = doctor.id
                INNER JOIN service_category ON service.service_category_id = service_category.id
            WHERE
                reception_line.id not in (SELECT reception_line_id FROM register)
            """)
            data = cur.fetchall()
            reception_lines = [ReceptionLine(
                                    id=row[0],
                                    reception_plan=ReceptionPlan(
                                        service=Service(
                                            id=row[1],
                                            name=row[2],
                                            service_category=ServiceCategory(
                                                id=row[3],
                                                name=row[4]
                                            )
                                        ),
                                        doctor=Doctor(
                                            id=row[5],
                                            first_name=row[6],
                                            last_name=row[7],
                                            middle_name=row[8]
                                        ),
                                        date=row[9]
                                    ),
                                    time=row[10]
            ) for row in data]
            return reception_lines, None
