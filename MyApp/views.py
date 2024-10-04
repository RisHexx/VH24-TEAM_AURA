from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/home")
@views.route("/")
def home():
    return "Home Page"

@views.route("/userhome", methods=['GET', 'POST'])
@login_required
def userhome():
    if current_user.is_authenticated:
        return render_template("userHome.html", user=current_user)
    else:
        return redirect(url_for('auth.login'))

@views.route("/orders", methods=['GET', 'POST'])
def orders():
    return "Orders Page"

@views.route("/leaderboard", methods=['GET', 'POST'])
def leaderboard():
    return render_template("leaderboard.html")

@views.route("/userdata", methods=['GET', 'POST'])
def userdata():
    return "UserData"
