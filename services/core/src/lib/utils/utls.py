import hashlib


def get_hash(string: str) -> str:
    return hashlib.sha512(string.encode('utf-8')).hexdigest()
