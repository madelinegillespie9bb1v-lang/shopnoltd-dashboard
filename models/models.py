from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    user_role = db.Column(db.String(50), default="user")
    is_verified = db.Column(db.Boolean, default=False)
    account_status = db.Column(db.String(50), default="inactive")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LoggedUser(db.Model):
    __tablename__ = "logged_users"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    login_time = db.Column(db.DateTime, default=datetime.utcnow)