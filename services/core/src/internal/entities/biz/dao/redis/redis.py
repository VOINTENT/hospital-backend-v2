from src.lib.drivers.redis.redis import r


def set_value(key, value):
    r.set(key, value)


def get_value(key):
    return r.get(key)