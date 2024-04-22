from app.extesiones import db

class Rango(db.Model):
    idRango = db.Column(db.Integer, primary_key=True)
    nombreRan = db.Column(db.String(45), nullable=True)