from sanic import Sanic

from .api.mainapi import main_api

app = Sanic("hospital_server_api", load_env=False)
app.blueprint(main_api)
