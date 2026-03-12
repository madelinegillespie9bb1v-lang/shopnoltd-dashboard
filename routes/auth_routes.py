from flask import Blueprint, render_template, request, redirect, flash, session
from extensions import db, mail
from models import User, LoggedUser
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message
import random

auth_bp = Blueprint("auth", __name__)

SESSION_LIFETIME_MINUTES = 60

@auth_bp.route("/")
def home():
    return render_template("index.html")

@auth_bp.route("/register.html", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if User.query.filter_by(email=email).first():
            flash("Email already registered. Please login.", "warning")
            return redirect("/login.html")

        hashed_password = generate_password_hash(password, method="sha256")
        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        # Generate OTP
        otp_code = str(random.randint(100000, 999999))
        session["otp"] = otp_code
        session["user_id"] = new_user.id

        try:
            msg = Message(
                subject="Your Shopnoltd OTP",
                sender=("Shopnoltd Support", "asaduzzaman.bheramara@gmail.com"),
                recipients=[email],
                body=f"Hello {username},\nYour OTP code is: {otp_code}"
            )
            mail.send(msg)
            flash("Registration successful! OTP sent to your email.", "success")
        except Exception as e:
            flash(f"Failed to send OTP email: {str(e)}", "danger")

        return redirect("/verify_otp.html")

    return render_template("register.html")

@auth_bp.route("/verify_otp.html", methods=["GET", "POST"])
def verify_otp():
    if request.method == "POST":
        otp_input = request.form.get("otp")
        user_id = session.get("user_id")
        session_otp = session.get("otp")

        if not user_id or not session_otp:
            flash("Session expired. Please register again.", "warning")
            return redirect("/register.html")

        if otp_input == session_otp:
            user = User.query.get(user_id)
            user.is_verified = True
            user.account_status = "active"
            db.session.commit()
            flash("OTP verified! You can now log in.", "success")
            session.pop("otp", None)
            session.pop("user_id", None)
            return redirect("/login.html")
        else:
            flash("Invalid OTP. Try again.", "danger")

    return render_template("verify_otp.html")

@auth_bp.route("/login.html", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash(f"Welcome, {user.username}!", "success")
            return redirect("/dashboard.html")
        else:
            flash("Invalid email or password", "danger")
            return redirect("/login.html")

    return render_template("login.html")

@auth_bp.route("/logout.html")
def logout():
    session.clear()
    flash("Logged out successfully", "info")
    return redirect("/login.html")