from flask import Flask , Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_login import LoginManager


db = SQLAlchemy()

def createapp():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "rishex"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/hackathon'
    db.init_app(app=app)
    from . import views

    from .views import views

    from .views import views
    from .auth import auth
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")
    return app