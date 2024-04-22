from app.extesiones import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date

Base = declarative_base()

class Audios(Base):
    __tablename__ = 'Audios'
    idAudios = Column(Integer, primary_key=True, autoincrement=True)
    fechaAud = Column(Date, nullable=True)
    Promotor_idPromotor = Column(Integer, ForeignKey('Promotor.idPromotor'), nullable=False)
    Promotor_Administrador_idAdministrador = Column(Integer, ForeignKey('Promotor.Administrador_idAdministrador'), nullable=False)
    Promotor_Rango_idRango = Column(Integer, ForeignKey('Promotor.Rango_idRango'), nullable=False)
    
    # Definiendo las relaciones con la tabla Promotor
    promotor = relationship("Promotor") 