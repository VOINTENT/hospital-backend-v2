from sanic import Sanic
from .middlewares.middlewares import add_cors
from .api.mainapi import main_api


def create_app():
    app = Sanic("hospital_server_api", load_env=False)
    app.blueprint(main_api)
    add_cors(app)
    return app
