from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Turnos(db.Model):
    idTurnos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numeroTur = db.Column(db.String(45), nullable=False)
    Promotor_idPromotor = db.Column(db.Integer, ForeignKey('promotor.idPromotor'), nullable=False)
