from flask import Blueprint

auth = Blueprint("auth",__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    return "Login Page"

@auth.route("/signup",methods=['GET','POST'])
def signup():
    return "SignUP Page"

@auth.route("/logoutpage")
def logout():
    return "LogOut"
