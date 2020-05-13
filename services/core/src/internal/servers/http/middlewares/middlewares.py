from inspect import isawaitable

from src.internal.servers.http.mainhttp import app


@app.middleware('response')
async def cors(request, response):
    if isawaitable(response):
        response = await response
    response.headers['Access-Control-Allow-Origin'] = 'localhost:3000'
    response.headers['Access-Control-Allow-Credentials'] = True

