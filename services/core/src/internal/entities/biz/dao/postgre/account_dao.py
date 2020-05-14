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

    def get_by_email_or_phone_number_and_password(self, email_or_phone_number: str, password: str) -> (None, bool):
        cur = self.conn.cursor()
        cur.execute(f"""
            SELECT COUNT(*)
            FROM account
            WHERE (email = '{email_or_phone_number}' OR phone_number = '{email_or_phone_number}') AND password = '{password}';
        """)
        data = cur.fetchall()
        print(data)
        cur.close()

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
