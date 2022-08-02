
from flask import Blueprint, Flask, render_template
from app.post.models import User, db

from sqlalchemy.orm import Session
app= Flask(__name__)

user_bp = Blueprint('user', __name__)
@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/cadastro')
def resp():
    return render_template('cad.html')

@app.route('/users')
def users():
    data = {
        'nome': "gerard",
        'sobrenome': "nunes",
        "email": "gerard@email",
        "senha": 00000
    }

    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()

    return User.query.all()





if __name__=="__main__":
    app.run(debug=True)

