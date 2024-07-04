from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Liquidos(db.Model):
    idLiquidos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreLiquido = db.Column(db.String(45), nullable=False)