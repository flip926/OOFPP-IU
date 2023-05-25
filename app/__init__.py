from flask import Flask
from .extension import db,migrate
from os import environ


def get_settings():
    return environ.get('SETTINGS')

def create_app():

    app = Flask(__name__)

    app.config.from_object(get_settings())


    db.init_app(app)
    migrate.init_app(app,db)

    from .habit import habit
    app.register_blueprint(habit,url_prefix='/')
    
    from . import models
    return app