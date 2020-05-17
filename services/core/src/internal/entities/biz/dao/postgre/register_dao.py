from src.internal.entities.biz.dao.interfaces.register_dao import RegisterDao
from src.internal.entities.biz.models.reception_line import ReceptionLine
from src.internal.entities.biz.models.register import Register


class RegisterDaoImpl(RegisterDao):
    """
    Данный класс является реализацией интерфейса AccDao, применимой для работы конкретно с PostgreSQL
    Каждый такой класс должен являться реализацией соответствующего интерфейса из пакета dao.interfaces
    """

    def add(self, register: Register) -> (Register or None, None or tuple):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO register(reception_line_id, patient_id) VALUES
                (%s, %s)
            """, (register.reception_line.id, register.patient.id))
            self.conn.commit()
            return register, None

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
