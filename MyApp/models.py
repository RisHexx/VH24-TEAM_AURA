from . import db
from datetime import datetime
from flask_login import UserMixin  

class Users(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)  
    email = db.Column(db.String(50), nullable=False, unique=True) 
    password = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, default=0)  
    orders = db.Column(db.Integer, default=0)  

    def __repr__(self):
        return f'<User {self.username}>'

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    order_name = db.Column(db.String(100), nullable=False)  
    order_time = db.Column(db.DateTime, default=datetime.utcnow)
    order_status = db.Column(db.String(50), nullable=False, default="Pending")  # Adding order status
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to Users table

    def __repr__(self):
        return f'<Order {self.order_name}>'

