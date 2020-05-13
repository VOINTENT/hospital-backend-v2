from src.internal.servers.http.mainhttp import app
from src.configs.server_settings import HOST, PORT, DEBUG, SSL, WORKERS, ACCESS_LOG


def main():
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
        ssl=SSL,
        workers=WORKERS,
        access_log=ACCESS_LOG
    )


if __name__ == '__main__':
    main()
