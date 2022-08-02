from datetime import datetime
from app.core import db

class User(db.Model):
    __tablename__= 'user'
    id = db.column("id", db.Integer)
    nome = db.column((db.String(20)))
    sobrenome = db.column((db.String(10)))
    email = db.column((db.String(90)))
    senha = db.column("id", db.Integer)

    @staticmethod
    def list_all():
        return User.query.all()

