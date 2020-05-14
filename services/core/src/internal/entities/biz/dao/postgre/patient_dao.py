from src.internal.entities.biz.dao.interfaces.patient_dao import PatientDao
from src.internal.entities.biz.models.patient import Patient


class PatientDaoImpl(PatientDao):

    def get_by_id(self, id: int) -> (object, bool):
        return super().get_by_id(id)

    def add(self, patient: Patient) -> (Patient, bool):
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO patient(account_id, first_name, last_name, middle_name, gender, birth_date) 
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
            """, (patient.account.id, patient.first_name, patient.last_name, patient.middle_name, 1,
                  patient.birth_date))
            self.conn.commit()
            patient.id = cur.fetchall()[0][0]
            return patient, False

    def remove(self, obj: object) -> (None, bool):
        return super().remove(obj)

    @staticmethod
    def remove_by_id(id: int) -> (None, bool):
        return super().remove_by_id(id)

    def get_all(self) -> (list, bool):
        return super().get_all()