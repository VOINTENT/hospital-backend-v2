import hashlib
import os
import jwt
import datetime


def get_hash(string: str) -> str:
    return hashlib.sha512(string.encode('utf-8')).hexdigest()


def get_token(account) -> str:
    secret_key = os.environ['SECRET_KEY'] if 'SECRET_KEY' in os.environ else 'qwerty123'
    return jwt.encode({'id': account.id, 'timestamp': datetime.datetime.today().timestamp()}, secret_key, algorithm='HS256').decode()


def get_payload(token: str) -> dict or None:
    try:
        secret_key = os.environ['SECRET_KEY'] if 'SECRET_KEY' in os.environ else 'qwerty123'
        return jwt.decode(token, secret_key, algorithm='HS256')
    except Exception:  # TODO
        return None


def serialize_date(date: datetime.date):
    if not date:
        return None

    day = str(date.day)
    month = str(date.month)
    year = str(date.year)
    return day + '-' + month + '-' + year


def serialize_time(time: datetime.time):
    if not time:
        return None

    return str(time)[:5]
