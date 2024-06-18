from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.extensiones import db
from flask_login import LoginManager
login_manager = LoginManager()

#can i esto? si


def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'Administrador.login'
    
    @login_manager.user_loader
    def load_user(idUser): # Flask-Login intentará cargar al usuario actual basándose en su identificador.
        from app.models.Administrador import Administrador
        from app.models.Promotor import Promotor
        from app.models.MetodosPago import MetodosPago
        from app.routes.Administradores_routes import tipo #try
        
        print(tipo)
        
        if tipo == 0 : 
             return Promotor.query.get(int(idUser))
        elif tipo == 1 : 
             return Administrador.query.get(int(idUser))
        

    
      
        
        # since the user_id is just the primary key of our user table, use it in the query for the user
       
    

    from app.routes import Administradores_routes, Promotor_routes, MetodosPago_routes
    app.register_blueprint(Administradores_routes.bp)
    app.register_blueprint(Promotor_routes.bp)
    app.register_blueprint(MetodosPago_routes.bp)
  
    
    
#tiene otro login like this ?, solo el de el otro trabajo, el de arriba a ver    

    return app