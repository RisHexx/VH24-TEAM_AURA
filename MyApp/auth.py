from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user
from . import db
from .models import Users

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email=email).first()
        if not user:
            return "User does not exist"
        elif not password:
            return "Password can't be blank"  
        else:
            if password == user.password:
                login_user(user)
                return redirect(url_for('views.userhome'))  
            else:
                return "Wrong credentials"
    return render_template("login.html")

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        
        if not username:
            return "Invalid username"
        elif not email:
            return "Invalid email"
        elif not password or not repassword:
            return "Password can't be blank"
        elif password != repassword:
            return "Passwords do not match"
        else:
            new_user = Users(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.userhome'))  
    return render_template("signup.html")

@auth.route("/logout")
def logout():
    return "You have been logged out"
