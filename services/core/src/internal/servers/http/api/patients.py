from sanic import Blueprint
from sanic.response import json

from .auth import auth

patients = Blueprint.group(auth, url_prefix='/patients')
patients_loc = Blueprint('patients', url_prefix='/patients')


@patients_loc.route('/')
async def patient_detail(request):
    return json({'answer': 'patients'})
