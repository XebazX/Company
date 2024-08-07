from app import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Date

class Promotor(db.Model, UserMixin):
    idPromotor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrePro = db.Column(db.String(45), nullable=False)
    numeroPro = db.Column(db.String(45), nullable=False)
    correoPro = db.Column(db.String(45), nullable=False)
    documentoPro = db.Column(db.String(45), nullable=False)
    contrasenaPro = db.Column(db.String(256), nullable=False)
    
    cierres = relationship('Cierre', backref='promotor', lazy=True)
    
    #lets try wait a minute, estare intentando algo
    
    
    @property
    def pl(self):
        return self.nombrePro[0] if self.nombrePro else None
    
    def get_id(self):
        return str(self.idPromotor)
    #cambielo a True dropppperdverrrrrrrrdaaaaaaaaaaaaaa
    
    
    #si se cambian a string servira o q, o acomodar la columna?
    #q ya que está cambie tambien la de documento que es parecido a lo que pasa con celular
    #Lo idea seria que hiciera el modelo en workbench pero no lo sincroniza, luego hace los modelos y al ejecutar el programa se crea la db, respecto a las columnas deberían ser str o -> 
    #en mysql no se cambia o q, o  como le haciamos con el profe, pur cambiar de bases de datos
    #-> tiene todos los modelos ya creados? y co?mpletos con foranea y demás? -> se supone -> lo que puede hacer es dropear la db y luego ejecutar el programa ->