from flask import Flask
import os
from app.extensiones import db
 



def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)

   
    
    
      
        
        # since the user_id is just the primary key of our user table, use it in the query for the user
       
    

    from app.routes import Administradores_routes, Promotor_routes, Rango_routes, Audios_routes
    app.register_blueprint(Administradores_routes.bp)
    app.register_blueprint(Promotor_routes.bp)
    app.register_blueprint(Rango_routes.bp)
    app.register_blueprint(Audios_routes.bp)
    
    
    

    return app