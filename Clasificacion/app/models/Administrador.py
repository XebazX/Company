from app.extensiones import db
from app import db
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

class  Administrador(db.Model):
    idAdministrador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreAdm = db.Column(db.String(45), nullable=False)
    numeroAdm = db.Column(db.Integer, nullable=False)
    correoAdm = db.Column(db.String(45), nullable=False)
    documentoAdm = db.Column(db.Integer, nullable=False)