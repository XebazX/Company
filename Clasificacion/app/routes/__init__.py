from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import Administradores_routes,  Promotor_routes, MetodosPago_routes

