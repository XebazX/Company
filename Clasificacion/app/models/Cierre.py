from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Cierre(db.Model):
    idCierre = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fechaCierre = db.Column(db.String(45), nullable=False)
    Promotor_idPromotor = db.Column(db.Integer, ForeignKey('promotor.idPromotor'), nullable=False)
    totalMetodo = db.Column(db.String(45), nullable=False)
    totalcierre = db.Column(db.String(45), nullable=False)

    detalles_mediospago = relationship('DetalleMediospago', backref='cierre', lazy=True)
    detalles_liquidos = relationship('DetalleLiquidos', backref='cierre', lazy=True)
    detalles_varios = relationship('DetalleVarios', backref='cierre', lazy=True)