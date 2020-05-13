import src.internal.instances.dbs as dbs
import src.internal.instances.http as http
from src.internal.servers.http.mainhttp import create_app
from src.configs.server_settings import *


def create_server():
    app = create_app()
    http.set_main_app(app)


def run_server():
    http.main_app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
        ssl=SSL,
        workers=WORKERS,
        access_log=ACCESS_LOG,
        auto_reload=AUTO_RELOAD
    )


def add_listeners():
    @http.main_app.listener('after_server_start')
    async def notify_server_started(app, loop):
        print('Server successfully started!')

    @http.main_app.listener('before_server_stop')
    async def notify_server_stopping(app, loop):
        print('Server shutting down!')

    @http.main_app.listener('after_server_stop')
    async def close_db(app, loop):
        if dbs.main_pgsql_connect is not None:
            dbs.main_pgsql_connect.close()
            print('Pgsql connection closed!')
