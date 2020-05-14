from inspect import isawaitable
from sanic.response import text


def add_cors(app):
    @app.middleware('response')
    async def cors_headers(request, response):
        if isawaitable(response):
            response = await response
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000' 
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Request-Methods'] = '*'

    @app.middleware('request')
    async def cors_options(request):
        if isawaitable(request):
            request = await request
        
        if request.method == 'OPTIONS':
            return text('ok')
