from sanic import Blueprint

from .patients import patients

entities = Blueprint.group(patients, url_prefix='/entities')
