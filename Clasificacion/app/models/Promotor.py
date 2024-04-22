from app.extesiones import db
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Date

class Promotor(db.Model):
    idPromotor = db.Column(Integer, primary_key=True, autoincrement=True)
    nombrePro = db.Column(String(45), nullable=False)
    numeroPro = db.Column(Integer, nullable=False)
    correoPro = db.Column(String(45), nullable=False)
    documentoPro =db. Column(Integer, nullable=False)
    Administrador_idAdministrador = db.Column(Integer, ForeignKey('Administrador.idAdministrador'), nullable=False)
    Rango_idRango = db.Column(Integer, ForeignKey('Rango.idRango'), nullable=False)
    
    # Definiendo las relaciones con las tablas Administrador y Rango
    administrador = relationship("Administrador")
    rango = relationship("Rango")