from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    user_role = db.Column(db.String(20), default="user")
    is_verified = db.Column(db.Boolean, default=False)
    account_status = db.Column(db.String(20), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LoggedUser(db.Model):
    __tablename__ = "logged_users"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    device_name = db.Column(db.String(100))
    device_model = db.Column(db.String(100))
    device_os = db.Column(db.String(100))
    ip_address = db.Column(db.String(100))
    login_time = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship("User", backref=db.backref("logins", lazy=True))