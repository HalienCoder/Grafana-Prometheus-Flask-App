from flask import Blueprint,render_template,request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    #when we use the request variable inside the route, it will have information about the request that was sent to access the route, like the URL, the method, all the info that was sent
    # the form attirubte of the request has all of the data that was sent as a part of a form.
    # LINE OF CODE => data=request.form

    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

            
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email = email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) <4 :
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 4 :
            flash('First name must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash("Passwords do not match", category='error')
        elif len(password1) < 7 :
            flash('Password must be greater than 7 charcaters.', category='error')
        else:
            #add user to db
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash ('Account created!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        
    return render_template("signup.html", user=current_user)