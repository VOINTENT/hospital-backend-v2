from sanic import Blueprint

from src.internal.servers.http.api.doctors import doctors
from .patients import patients

entities = Blueprint.group(patients, doctors, url_prefix='/entities')
