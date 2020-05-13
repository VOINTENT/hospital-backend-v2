from src.internal.instances.dbs import set_pgsql_connect
from src.lib.drivers.pgsqldrv.pgsqldrv import create_conn
from src.configs.pgsql_settings import *


def create_pgsql_conn():
    conn = create_conn(HOST, PORT, DB_NAME, USER, PASSWORD)
    set_pgsql_connect(conn)
