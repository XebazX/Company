from app import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Date

class Promociones(db.Model):
    __tablename__ = 'promociones'
    idPromociones = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrePromocion = db.Column(db.String(45), nullable=False) #que pro