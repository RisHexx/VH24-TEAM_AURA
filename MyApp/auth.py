from flask import Blueprint , render_template

auth = Blueprint("auth",__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    return render_template("index.html")

@auth.route("/signup",methods=['GET','POST'])
def signup():
    return "SignUP Page"

@auth.route("/logoutpage")
def logout():
    return "LogOut"
