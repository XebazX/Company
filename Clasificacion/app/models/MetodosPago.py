from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class MetodosPago(db.Model):
    __tablename__ = 'metodospago'
    idMetodosPago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombreMetodo = db.Column(db.String(45), nullable=False)

    #ya cambie de todo en eso y sepa

  