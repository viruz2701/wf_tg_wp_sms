from flask import Flask
from flask_login import LoginManager
from app.config import Config
from app.database import init_db
from app.controllers.auth_controller import auth_bp
from app.controllers.admin_controller import admin_bp
from app.controllers.client_controller import client_bp
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    CSRFProtect(app)

    app.config.from_object(Config)
    
    init_db(app)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(client_bp)
    
    return app
    
    

def create_app():
    app = Flask(__name__)
    # ... существующий код ...
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app