from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from website.database import User
from werkzeug.security import generate_password_hash, check_password_hash
import re
from website import db
from flask_login import login_user, login_required, logout_user, current_user





auth = Blueprint('auth', __name__)
re_email = re.compile(r'^([a-zA-Z0-9\\_\\-\\.]+)@([a-zA-Z]+).(.+)$')
re_password = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[?!@#$%^&*-+]).{8,}$')


# Login Page
@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user)




# Register Page
@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method =='POST':
        username = request.form.get('username')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        birthday = request.form.get('birthday')
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password2')


        # Conditions for email registration
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email has already been used for an account.', category='error')
        elif not re.fullmatch(re_email, email):
            flash('Email does not meet requirements', category='error')            
        elif not re.fullmatch(re_password, password):
            flash('Password should contain at least 8 characters, one uppercase, one lowercase, one number, and one special character (?!@#$%^&*-+).', category='error')
        elif password2 != password:
            flash('Password does not match.', category ='error')
        else:
            # Create new user account and add to the database
            new_user = User(
            username=username, 
            firstName=firstName, 
            lastName=lastName, 
            birthday=birthday, 
            email=email, 
            password=generate_password_hash(password, method='sha256')
            )

            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')

            return redirect(url_for('auth.login'))

    return render_template("register.html", user=current_user)


# Logout Page
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
