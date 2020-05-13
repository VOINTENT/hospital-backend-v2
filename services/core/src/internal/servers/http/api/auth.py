from sanic import Blueprint
from sanic.response import json

auth = Blueprint('auth', url_prefix='/auth')


@auth.route('/login/basic')
async def patient_login(request):
    return json({'answer': 'patients'})


@auth.route('/signup')
async def patient_login(request):
    return json({'answer': 'patients'})


@auth.route('/logout')
async def patient_login(request):
    return json({'answer': 'patients'})
