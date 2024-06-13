from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationships

class DetalleVarios(db.Model):
    idDetalleVarios = db.Column(db.Integer, primary_key=True, autoincrement=True)
    totalVarios = db.Column(db.String(45), nullable=False)
    Cierre_idCierre = db.Column(db.Integer, ForeignKey('cierre.idCierre'), nullable=False)
    Cierre_Promotor_idPromotor = db.Column(db.Integer, ForeignKey('promotor.idPromotor'), nullable=False)
    Varios_idVarios = db.Column(db.Integer, ForeignKey('varios.idVarios'), nullable=False)