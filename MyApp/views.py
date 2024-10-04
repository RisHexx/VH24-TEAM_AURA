from flask import Blueprint , render_template , request , flash , redirect , url_for
from flask_login import login_required , current_user

views = Blueprint("views",__name__)

@views.route("/")
def home():
    return "Home Page"

@views.route("/user",methods=['GET','POST'])
def userhome():
    return "User Home Page"

@views.route("/orders",methods=['GET','POST'])
def orders():
    return "Orders Page"

@views.route("/leaderboard",methods=['GET','POST'])
def leaderboard():
    return "Leader Board"

@views.route("/userdata",methods=['GET','POST'])
def userdata():
    return "UserData"

