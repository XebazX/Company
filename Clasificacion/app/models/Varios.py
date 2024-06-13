from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Varios(db.Model):
    idVarios = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreVarios = db.Column(db.String(45), nullable=False)
    cantidadVarios = db.Column(db.String(45), nullable=False)
    totalVarios = db.Column(db.String(45), nullable=False)