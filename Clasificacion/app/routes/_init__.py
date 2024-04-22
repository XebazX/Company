from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import Administrador_routes, Categoria_routes, Cliente_routes, Detalle_routes, Factura_routes, Productos_routes