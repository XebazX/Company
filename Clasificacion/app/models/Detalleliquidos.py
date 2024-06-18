from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class DetalleLiquidos(db.Model):
    __tablename__ = 'DetalleLiquidos'
    idDetalleLiquidos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    totalLiq = db.Column(db.String(45), nullable=False)
    Cierre_idCierre = db.Column(db.Integer, ForeignKey('cierre.idCierre'), nullable=False)
    Cierre_Promotor_idPromotor = db.Column(db.Integer, ForeignKey('promotor.idPromotor'), nullable=False)
    Liquidos_idLiquidos = db.Column(db.Integer, ForeignKey('liquidos.idLiquidos'), nullable=False)