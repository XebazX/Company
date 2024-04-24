from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.extensiones import db
from flask_login import LoginManager
login_manager = LoginManager()



def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'Administrador.login'
    
    @login_manager.user_loader
    def load_user(idUser): # Flask-Login intentará cargar al usuario actual basándose en su identificador.
        from .models.Administrador import Administrador
        from .models.Promotor import Promotor
        from .routes.Administrador_routes import tipo
        
        if tipo == 0 : 
             return Promotor.query.get(int(idUser))
        elif tipo == 1 : 
             return Administrador.query.get(int(idUser))
        

    
      
        
        # since the user_id is just the primary key of our user table, use it in the query for the user
       
    

    from app.routes import Administradores_routes, Promotor_routes, Rango_routes, Audios_routes
    app.register_blueprint(Administradores_routes.bp)
    app.register_blueprint(Promotor_routes.bp)
    app.register_blueprint(Rango_routes.bp)
    app.register_blueprint(Audios_routes.bp)
    
    
    

    return app