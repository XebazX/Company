from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class DetalleTurno(db.Model):
    __tablename__ = 'detalleTurno'
    iddetalleTurno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    promotor_idPromotor = db.Column(db.Integer, db.ForeignKey('promotor.idPromotor'), nullable=False)
    turnos_idTurnos = db.Column(db.Integer, db.ForeignKey('turnos.idTurnos'), nullable=False)