from inspect import isawaitable


def add_cors(app):
    @app.middleware('response')
    async def cors(request, response):
        if isawaitable(response):
            response = await response
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000' 
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Request-Method'] = 'GET,POST,PUT,DELETE,OPTIONS'
