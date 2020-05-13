from sanic import Blueprint

from .entities import entities

main_api = Blueprint.group(entities, url_prefix='/api/v1')
