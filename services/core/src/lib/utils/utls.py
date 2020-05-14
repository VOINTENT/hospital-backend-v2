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
