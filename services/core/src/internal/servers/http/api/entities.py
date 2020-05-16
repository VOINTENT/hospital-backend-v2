from sanic import Blueprint

from src.internal.servers.http.api.doctors import doctors
from src.internal.servers.http.api.service_category import service_categories
from src.internal.servers.http.api.services import services
from .patients import patients

entities = Blueprint.group(patients, doctors, service_categories, services, url_prefix='/entities')
