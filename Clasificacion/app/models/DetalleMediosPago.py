from app.extensiones import db
from flask_login import UserMixin
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class DetalleMediospago(db.Model):
    idDetalleMediospago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    totalPago = db.Column(db.String(45), nullable=False)
    Cierre_idCierre = db.Column(db.Integer, ForeignKey('cierre.idCierre'), nullable=False)
    Cierre_Promotor_idPromotor = db.Column(db.Integer, ForeignKey('promotor.idPromotor'), nullable=False)
    Metodospago_idMetodospago = db.Column(db.Integer, ForeignKey('metodospago.idMetodosPago'), nullable=False)

#q necesita algo, como era pa el cursor que titirea? osea la mrda este de texto no el cursor dejelo al frio y empieza a A WAIT Y MIRO osea como lo habiamos configurado