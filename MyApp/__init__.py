from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def createapp():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "rishex"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/hackathon'
    
    db.init_app(app)
    login_manager.init_app(app)  
    login_manager.login_view = 'auth.login'  

   
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import Users 
    return Users.query.get(int(user_id))  
