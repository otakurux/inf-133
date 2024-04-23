from flask import Blueprint, request, redirect, url_for
from views import user_view
from models.user_model import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def usuarios():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route('/users', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        password = request.form['password']
        user = User(first_name, last_name, email, date_of_birth, password) #
        user.save()
        return redirect(url_for('user.usuarios'))
    return user_view.registro()
