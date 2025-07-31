#initializing flask wpp
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vistae.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    # Import and register Blueprints
    from app_code.routes import auth, dashboard, proctoring
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(proctoring.bp)

    return app

