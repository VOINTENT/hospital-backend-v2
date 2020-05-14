from src.internal.entities.biz.models.patient import Patient
from src.internal.errors.login import WRONG_EMAIL_OR_PHONE_NUMBER
from ..interfaces.account_dao import AccountDao
from src.internal.entities.biz.models.account import Account


class AccountDaoImpl(AccountDao):
    """
    Данный класс является реализацией интерфейса AccDao, применимой для работы конкретно с PostgreSQL
    Каждый такой класс должен являться реализацией соответствующего интерфейса из пакета dao.interfaces
    """

    def get_by_id(self, id: int) -> (Account, bool):
        pass

    def add(self, account: Account) -> (Account, bool):
        with self.conn.cursor() as cur:
            cur.execute("""
            INSERT INTO account(email, phone_number, password, is_active, user_type) 
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
            """, (account.email, account.phone_number, account.password, True, 'patient'))
            self.conn.commit()
            account.id = cur.fetchall()[0][0]
            return account, False

    def remove(self, acc: Account) -> (None, bool):
        pass

    def remove_by_id(self, id: int) -> (None, bool):
        pass

    def get_all(self) -> (list, bool):
        pass

    def get_by_email_or_phone_number_and_password(self, email_or_phone_number: str, password: str) -> (None, None):
        with self.conn.cursor() as cur:
            cur.execute(f"""
                SELECT email, phone_number, patient.id, account_id, first_name, last_name, middle_name, gender, 
                birth_date, snils, policy
                FROM account INNER JOIN patient ON account.id = patient.account_id
                WHERE account.user_type = 'patient' AND (account.email = %s OR account.phone_number = %s) 
                AND account.password = %s;
            """, (email_or_phone_number, email_or_phone_number, password))
            data = cur.fetchall()
            if len(data) == 0:
                return None, WRONG_EMAIL_OR_PHONE_NUMBER

            patient_data = data[0]
            return Patient(
                id=patient_data[2],
                account=Account(
                    id=patient_data[3],
                    email=patient_data[0],
                    phone_number=patient_data[1]
                ),
                first_name=patient_data[4],
                last_name=patient_data[5],
                middle_name=patient_data[6],
                gender=patient_data[7],
                birth_date=patient_data[8],
                snils=patient_data[9],
                policy=patient_data[10]
            ), None

    def is_email_exists(self, email):
        cur = self.conn.cursor()
        cur.execute(f"""
            SELECT COUNT(*)
            FROM account
            WHERE email = %s
        """, (email,))
        data = cur.fetchall()
        if data[0][0] == 0:
            return False
        return True

    def is_phone_number_exists(self, phone_number):
        cur = self.conn.cursor()
        cur.execute(f"""
                    SELECT COUNT(*)
                    FROM account
                    WHERE phone_number = %s
                """, (phone_number,))
        data = cur.fetchall()
        if data[0][0] == 0:
            return False
        return True
