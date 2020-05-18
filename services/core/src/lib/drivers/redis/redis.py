import redis

from src.configs.redis_settings import *

r = redis.Redis(host=HOST, port=PORT, db=DB_NAME)