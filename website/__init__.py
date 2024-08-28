from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager

from dotenv import load_dotenv

db = SQLAlchemy()
DB_NAME= "basetooter.db"
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # importing blueprints
    from website.views import views
    from website.auth import auth

    # register with no prefix
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # create database if there is none
    with app.app_context():
        create_database()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from website.database import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app


# create a new database if it does not exist
def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all()
