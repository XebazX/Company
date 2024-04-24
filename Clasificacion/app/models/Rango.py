from app import db

class Rango(db.Model):
    __tablename__ = "Rangos"
    idRango = db.Column(db.Integer, primary_key=True)
    nombreRan = db.Column(db.String(45), nullable=True)
    