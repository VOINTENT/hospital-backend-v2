from src.internal.instances.http import main_app
from src.configs.server_settings import HOST, PORT, DEBUG, SSL, WORKERS, ACCESS_LOG, AUTO_RELOAD


def main():
    main_app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
        ssl=SSL,
        workers=WORKERS,
        access_log=ACCESS_LOG,
        auto_reload=AUTO_RELOAD
    )


if __name__ == '__main__':
    main()
