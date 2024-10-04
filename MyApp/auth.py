from flask import Blueprint , render_template , request , redirect , url_for
from . import db
from .models import Users
auth = Blueprint("auth",__name__)

@auth.route("/login",methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = Users.query.filter_by(email = email).first()
        if not user:
            return("User Nor exist",'error')
        elif not password:
            return("password Can't Be Blank" , 'error')
        else:
            if password == user.password:
                return redirect(url_for('views.home'))
            else:
                return("Wrong Credentials",'error')
    return render_template("login.html")

@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if not username:
            return("Invalid User Name ")
        elif not email:
            return("Invalid User Name ")
        elif not password and not repassword:
            return("Password Cant be Blank")
        elif password != repassword:
            return("Password Not Matching",'error')
        else:
            new_user = Users(username = username , email = email , password = password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))
    return render_template("signup.html")

@auth.route("/logoutpage")
def logout():
    return "LogOut"
