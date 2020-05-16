from src.internal.entities.biz.dao.interfaces.patient_dao import PatientDao
from src.internal.entities.biz.models.account import Account
from src.internal.entities.biz.models.patient import Patient
from src.internal.errors.common import ACCOUNT_NOT_FOUND


class PatientDaoImpl(PatientDao):

    def add(self, patient: Patient) -> (Patient or None, bool):
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO patient(account_id, first_name, last_name, middle_name, gender, birth_date) 
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
            """, (patient.account.id, patient.first_name, patient.last_name, patient.middle_name, 1,
                  patient.birth_date))
            self.conn.commit()
            patient.id = cur.fetchall()[0][0]
            return patient, False

    def get_by_account_id(self, account_id: int) -> (Patient or None, tuple or None):
        with self.conn.cursor() as cur:
            cur.execute(f"""
                SELECT patient.id, account_id, email, phone_number, first_name, last_name, middle_name, gender, 
                birth_date, snils, policy
                FROM account INNER JOIN patient ON account.id = patient.account_id
                WHERE account.user_type = 'patient' AND account.id = %s;
            """, (account_id, ))
            data = cur.fetchall()
            if len(data) == 0:
                return None, ACCOUNT_NOT_FOUND

            patient_data = data[0]
            return Patient(
                id=patient_data[0],
                account=Account(
                    id=patient_data[1],
                    email=patient_data[2],
                    phone_number=patient_data[3]
                ),
                first_name=patient_data[4],
                last_name=patient_data[5],
                middle_name=patient_data[6],
                gender=patient_data[7],
                birth_date=patient_data[8],
                snils=patient_data[9],
                policy=patient_data[10]
            ), None

    def update(self, patient: Patient) -> (Patient or None, tuple or None):
        with self.conn.cursor() as cur:
            try:
                SQL_UPDATE = """
                UPDATE patient
                SET 
                """

                updated_values = []

                if patient.first_name is not None:
                    SQL_UPDATE += ', ' if updated_values else ''
                    SQL_UPDATE += 'first_name = %s'
                    updated_values.append(patient.first_name)

                if patient.last_name is not None:
                    SQL_UPDATE += ', ' if updated_values else ''
                    SQL_UPDATE += 'last_name = %s'
                    updated_values.append(patient.last_name)

                if patient.middle_name is not None:
                    SQL_UPDATE += ', ' if updated_values else ''
                    SQL_UPDATE += 'middle_name = %s'
                    updated_values.append(patient.middle_name)

                if patient.gender is not None:
                    SQL_UPDATE += ', ' if updated_values else ''
                    SQL_UPDATE += 'gender = %s'
                    updated_values.append(patient.gender)

                if patient.birth_date is not None:
                    SQL_UPDATE += ', ' if updated_values else ''
                    SQL_UPDATE += 'birth_date = %s'
                    updated_values.append(patient.birth_date)

                if patient.snils is not None:
                    SQL_UPDATE += ', ' if updated_values else ''
                    SQL_UPDATE += 'snils = %s'
                    updated_values.append(patient.snils)

                if patient.policy is not None:
                    SQL_UPDATE += ', ' if updated_values else ''
                    SQL_UPDATE += 'policy = %s'
                    updated_values.append(patient.policy)

                if not updated_values:
                    return patient, None

                SQL_UPDATE += """
                    WHERE account_id = %s
                    RETURNING id
                """
                updated_values.append(patient.account.id)

                cur.execute(SQL_UPDATE, updated_values)
                self.conn.commit()
                if not cur.fetchall():
                    return None, ACCOUNT_NOT_FOUND
                return patient, None
            except:
                self.conn.commit()
