from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:localhost/test'
    bootstrap.init_app(app)
    app.static_folder = 'static'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
