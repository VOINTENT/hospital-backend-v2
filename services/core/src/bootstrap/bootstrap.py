from .dbs import create_pgsql_conn
from .servers import create_server, run_server, add_listeners

from src.internal.instances.http import main_app


def init_all():
    create_pgsql_conn()
    print('Pgsql connection created!')

    create_server()
    print('Server created!')

    add_listeners()
    print('Listeners added!')

    run_server()
