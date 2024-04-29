from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

class  Administrador(db.Model, UserMixin):
    idAdministrador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreAdm = db.Column(db.String(45), nullable=False)
    numeroAdm = db.Column(db.String(45), nullable=False)
    correoAdm = db.Column(db.String(45), nullable=False) # lo cambio aqui pero en la db sigue en okintokokokokokok
    documentoAdm = db.Column(db.String(45), nullable=False) # Aqui pasa lo mismo que con el promotor y es que el numero y el documento debe ser strings por eso dice el error que,
    contrasenaAdm = db.Column(db.String(256), nullable=False) # vamooooooo    
    
    
    
    def get_id(self):
        return str(self.idAdministrador)
    #tomare ss de la db por si acaso