from sanic import Blueprint
from sanic.response import json

from src.internal.entities.biz.validators.login import LoginSchema
from src.internal.servers.http.answer import get_response
from src.internal.servers.http.answer import get_response_with_validation_mistakes

auth = Blueprint('auth', url_prefix='/auth')


@auth.route('/login/basic', methods=['POST'])
async def patient_login(request):
    data = request.form

    mistakes = LoginSchema().validate(data)
    if mistakes:
        return json(get_response_with_validation_mistakes(mistakes), 400)

    return json({'answer': 'patients'})


@auth.route('/signup')
async def patient_login(request):
    return json({'answer': 'patients'})


@auth.route('/logout')
async def patient_login(request):
    return json({'answer': 'patients'})


@auth.route('/restore-password')
async def patient_restore_password(request):
    return json({'answer': 'patients'})