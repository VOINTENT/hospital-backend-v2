from typing import Any


def get_response(status: int or None = None, msg: str or None = None, data: Any = None):
    return {
        'status': status,
        'msg': msg,
        'data': data
    }