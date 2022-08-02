import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


db = SQLAlchemy()
migrate = Migrate()


def create_app(teste_config=None):
    app= Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite://users.sqlite3'
    app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db )


    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.post.cale import user_bp
    app.register_blueprint(user_bp)



