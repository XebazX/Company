from app import db
#esa mamada


#! Soy yo o el init que está dentro de models lefalta _ -> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA  COÑO E LA MADRE DENUVO DROP Y DEMÁS, YA SE!!!!     xde hagalos ps weon 

#now drop and create <- devuelta 


class Audios(db.Model):
    __tablename__ = 'Audios'
    idAudios = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fechaAud = db.Column(db.Date, nullable=True)
    Promotor_idPromotor = db.Column(db.Integer, db.ForeignKey('promotores.idPromotor'), nullable=False)
     #asique hace, esas foraneas no se usan,entendeu? oka -> 
    # Definiendo las relaciones con la tabla Promotor, xde like you?nossa cara
    
    promotor = db.relationship("Promotor") #que paso? xde
    #que falta? -> lets try lo , no salio el modelo de audio won 
    
    #El caso es que ni siquiera lo está tomando sqlalchemy por eso no aparece erros o menos se crea