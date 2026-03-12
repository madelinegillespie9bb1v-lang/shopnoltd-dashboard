from flask import Blueprint, render_template

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard.html")
def dashboard():
    return render_template("dashboard.html")

@dashboard_bp.route("/admindashboard.html")
def admindashboard():
    return render_template("admindashboard.html")

@dashboard_bp.route("/kobodashboard.html")
def kobodashboard():
    return render_template("kobodashboard.html")