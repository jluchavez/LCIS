from flask import Blueprint, render_template, request, flash, redirect, url_for
from .flaskform import UsersForm
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db
import datetime
auth = Blueprint('auth', __name__)

# Homepage
@auth.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template("homepage.html", user=current_user)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                id = current_user.id
                if id == 1:
                    return redirect(url_for('views.query_patient'))
                else:
                    return redirect(url_for('views.user_profile'))
            else:
                flash('Incorrect password, try again.', 'error')
        else:
            flash('Email does not exist.', 'error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.homepage'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = Users.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', 'error')
        elif len(email) < 4:
            flash('Email must be  greater than 4 characters.', 'error')
        elif len(username) < 2:
            flash('username must be greater than 2 characters.', 'error')
        elif password1 != password2:
            flash('Password don\'t match.', 'error')
        elif len(password1) < 7:
            flash('Password must be atleast 7 characters.', 'error')
        else:
            #add user to the database
            new_user = Users(email=email, username=username, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!', 'success')
            return redirect(url_for('views.user_registration'))

    return render_template("sign_up.html", user=current_user)

