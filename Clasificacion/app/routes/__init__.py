from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import Administradores_routes, Audios_routes, Promotor_routes, Rango_routes

