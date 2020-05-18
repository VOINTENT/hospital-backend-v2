from typing import List

from src.internal.entities.biz.dao.interfaces.register_dao import RegisterDao
from src.internal.entities.biz.models.doctor import Doctor
from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.internal.entities.biz.models.reception_plan import ReceptionPlan
from src.internal.entities.biz.models.register import Register
from src.internal.entities.biz.models.service import Service
from src.internal.entities.biz.models.service_category import ServiceCategory
from src.internal.errors.common import DATABASE_MISTAKE
from src.internal.errors.register import TOO_MANY_REGISTERS


class RegisterDaoImpl(RegisterDao):
    """
    Данный класс является реализацией интерфейса AccDao, применимой для работы конкретно с PostgreSQL
    Каждый такой класс должен являться реализацией соответствующего интерфейса из пакета dao.interfaces
    """

    def add(self, register: Register) -> (Register or None, None or tuple):
        with self.conn.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO register(reception_line_id, patient_id) VALUES
                    (%s, %s)
                """, (register.reception_line.id, register.patient.id))
                self.conn.commit()
                return register, None
            except:
                self.conn.commit()
                return None, DATABASE_MISTAKE

    def is_reception_line_busy(self, reception_line: ReceptionLine) -> bool:
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(*)
                FROM register
                WHERE register.reception_line_id = %s
            """, (reception_line.id,))
            data = cur.fetchall()
            if data[0][0] != 0:
                return True
            return False

    def get_all_by_patient_id(self, patient_id: int) -> (List[Register] or None, None or tuple):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT register.id, reception_line.id, service.id, service.name, service_category.id, service_category.name, doctor.id, first_name, last_name, middle_name, date, time
                FROM register 
                    INNER JOIN reception_line ON register.reception_line_id = reception_line.id
                    INNER JOIN reception_plan ON reception_line.id = reception_plan.id 
                    INNER JOIN service ON reception_plan.service_id = service.id
                    INNER JOIN doctor ON reception_plan.doctor_id = doctor.id
                    INNER JOIN service_category ON service.service_category_id = service_category.id
                WHERE register.patient_id = %s
            """, (patient_id,))
            data = cur.fetchall()
            registers = [Register(
                id=row[0],
                reception_line=ReceptionLine(
                    id=row[1],
                    reception_plan=ReceptionPlan(
                        service=Service(
                            id=row[2],
                            name=row[3],
                            service_category=ServiceCategory(
                                id=row[4],
                                name=row[5]
                            )
                        ),
                        doctor=Doctor(
                            id=row[6],
                            first_name=row[7],
                            last_name=row[8],
                            middle_name=row[9]
                        ),
                        date=row[10]
                    ),
                    time=row[11]
                )
            ) for row in data]
            return registers, None

    def is_register_own_patient(self, register_id: int, patient_id: int) -> bool:
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT patient_id
                FROM register
                WHERE id = %s
            """, (register_id,))
            data = cur.fetchall()
            if data[0][0] != patient_id:
                return False
            return True

    def remove_by_id(self, register_id: int) -> (Register or None, None or tuple):
        with self.conn.cursor() as cur:
            try:
                cur.execute("""
                    DELETE 
                    FROM register
                    WHERE id = %s
                """, (register_id, ))
                self.conn.commit()
                return register_id, None
            except:
                self.conn.commit()
                return None, DATABASE_MISTAKE

    def is_patient_has_too_many_registers(self, patient_id: int) -> bool:
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT COUNT(*)
                FROM register
                WHERE patient_id = %s
            """, (patient_id, ))
            if cur.fetchall()[0][0] >= 3:
                return True
            return False

