from . import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, default=0)  # New score column with default value 0
    orders = db.Column(db.Integer, default=0)  # New score column with default value 0

    def __repr__(self):
        return f'<User {self.username}>'
    
from datetime import datetime

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key for Orders
    order_name = db.Column(db.String(100), nullable=False)  # Name of the order
    order_time = db.Column(db.DateTime)  # Time when the order was placed

    def __repr__(self):
        return f'<Order {self.order_name}>'




