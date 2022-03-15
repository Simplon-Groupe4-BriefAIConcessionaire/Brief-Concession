from importlib.resources import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
db_name = "voitures.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .model import Voitures

    
    create_database(app)

    return app

def create_database(app):
    if not path.exists('app' + db_name):
        db.create_all(app=app)