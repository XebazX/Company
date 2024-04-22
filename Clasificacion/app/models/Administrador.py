from app.extesiones import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class  Administrador(db.Model):
    idAdministrador = Column(Integer, primary_key=True, autoincrement=True)
    nombreAdm = Column(String(45), nullable=False)
    numeroAdm = Column(Integer, nullable=False)
    correoAdm = Column(String(45), nullable=False)
    documentoAdm = Column(Integer, nullable=False)